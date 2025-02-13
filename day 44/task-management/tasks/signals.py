from django.db.models.signals import post_save , pre_save , pre_delete , post_delete ,m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from tasks.models import Task

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

@receiver(post_delete , sender = Task)
def delete_associate_details(sender , instance , **kwargs):
    if isinstance:
        print(instance)
        if instance.details:
            instance.details.delete()
            print("deleted successfully ")