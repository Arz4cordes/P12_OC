from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    class Assignement(models.TextChoices):
        COMMERCIAL = 'Commercial'
        SUPPORT = 'Support'
        MANAGEMENT = 'Management'

    assignement = models.CharField(max_length=64, choices=Assignement.choices, default=Assignement.SUPPORT)
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    email = models.EmailField(max_length=256, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.email}"
