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
    is_active = True
    is_staff = False


class ManagementManager(models.Manager):
    def queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(assignement=User.Assignement.MANAGEMENT)


class ManagementTeam(User):
    objects = ManagementManager()

    is_staff = True

    class Meta:
        proxy = True


class CommercialManager(models.Manager):
    def queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(assignement=User.Assignement.COMMERCIAL)


class CommercialTeam(User):
    objects = CommercialManager()

    class Meta:
        proxy = True


class SupportManager(models.Manager):
    def queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(assignement=User.Assignement.SUPPORT)


class SupportTeam(User):
    objects = SupportManager()

    class Meta:
        proxy = True
