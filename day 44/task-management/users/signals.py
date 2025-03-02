from django.db.models.signals import post_save , pre_save , pre_delete , post_delete ,m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.contrib.auth import get_user_model
# from users.models import UserProfile

User = get_user_model()

@receiver(post_save , sender = User)
def send_activation_email(sender , instance , created , **kwargs):
    if created:
        token = default_token_generator.make_token(instance)
        activation_url = f"{settings.FRONTEND_URL}/users/activate/{instance.id}/{token}/"

        subject = "Activate your Account "
        message = f' Hi , {instance.username}\n\n Please activate your account by thin link : \n\n {activation_url}\n\n Thanks From Task Team'

        recipient_list = [instance.email]
        try : 
            send_mail(subject , message,settings.EMAIL_HOST_USER,recipient_list)
        except Exception as E:
            print(f"Failed to send email to {instance.email} : {str(E)}")

@receiver(post_save , sender=User)
def assign_role(sender , instance , created , **kwargs):
    if created:
        user_group , created = Group.objects.get_or_create(name="User") # 2ta parameter return kore .. akta Group ar akta boolean value ,, 
        instance.groups.add(user_group)
        instance.save()


"""
@receiver(post_save , sender=User)
def Create_or_update_user_profile(sender , instance , created , **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

"""