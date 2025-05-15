from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('job_seeker', 'Job Seeker'),
        ('recruiter', 'Recruiter'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username