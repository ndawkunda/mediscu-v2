# user-service/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class HealthcareProfessional(AbstractUser):
    specialization = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
