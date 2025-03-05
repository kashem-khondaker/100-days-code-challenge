from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User


# class Employee(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.name

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
        # on_delete=models.DO_NOTHING,
        # default=1
        
    )
    # employee = models.ManyToManyField(Employee ,related_name='task')
    employee = models.ManyToManyField(settings.AUTH_USER_MODEL ,related_name='task' )
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=15,choices=STATUS_CHOICES ,default='PENDING')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)  # Save Task first
    #     task_details, created = taskDetails.objects.get_or_create(task=self)


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
        # on_delete=models.CASCADE, 
        on_delete=models.DO_NOTHING, 
        default=1,
        related_name="details",
        # null=True,
        # blank=True
    )  
    # assign_to = models.CharField(max_length=200)
    priority = models.CharField(choices=PRIORITY_OPTIONS , default=Low)
    notes = models.TextField(blank=True , null=True)
    asset = models.ImageField(upload_to='task_asset' , blank=True , null=True , default='task_asset/download.png')

    def __str__(self):
        return f"Details form Task {self.task.title}"
    
