from django.db import models
from django.db.models.signals import post_save , pre_save , pre_delete , post_delete ,m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True , null=True)
    start_date = models.DateField()

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES =[
        ('PENDING' , 'Pending'),
        ("IN_PROGRESS" , 'In Progress'),
        ('COMPLETED' , 'Completed')
    ]
    project = models.ForeignKey(
        Project ,
        on_delete=models.CASCADE,
        default=1
    )
    employee = models.ManyToManyField(Employee ,related_name='task')
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=15,choices=STATUS_CHOICES ,default='PENDING')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class taskDetails(models.Model):
    High = 'High'
    Medium = 'Medium'
    Low = 'Low'
    PRIORITY_OPTIONS = (
        (High , 'High'),
        (Medium , 'Medium'),
        (Low , 'Low'),
    )
    
    task = models.OneToOneField(
        Task , 
        on_delete=models.CASCADE, 
        default=1,
        related_name="details"
    )  
    # assign_to = models.CharField(max_length=200)
    priority = models.CharField(choices=PRIORITY_OPTIONS , default=Low)
    notes = models.TextField(blank=True , null=True)

    def __str__(self):
        return f"Details form Task {self.task.title}"
    
    # @receiver(post_save , sender = Task)
    # def Notify_task_creation(sender , instance , created , **kwargs):
    #     if created:
    #         print(sender)
    #         print(instance)
    #         print(kwargs)
            
    #         instance.is_completed = True
    
    @receiver(m2m_changed , sender = Task.employee.through)
    def Notify_employee_on_task_creation(sender , instance , action,**kwargs):
        
        
        if action=="post_add":
            assigned_emails = [emp.email for emp in instance.employee.all()]
            print(assigned_emails)
            send_mail(
                "Checkout your new task ",
                f"You have been assigned to this task : {instance.title}",
                "kashem.khondaker.official001@gmail.com",
                assigned_emails,
                fail_silently=False,   # for show error when main not send !
            )



