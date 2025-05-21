from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        # Example: send welcome email (can be replaced with logging, etc.)
        send_mail(
            subject='Welcome to AI Job Matcher',
            message=f'Hi {instance.username}, thanks for signing up!',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            fail_silently=True,  # Prevent crashing if email fails
        )