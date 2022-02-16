from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.models import Group

# Create your models here.


class MyUserManager(UserManager):
    def create_user(self,
                    username,
                    first_name,
                    last_name,
                    email,
                    assignement,
                    password=None):
        my_user = self.model(username=username,
                          first_name=first_name,
                          last_name=last_name,
                          email=email,
                          assignement=assignement)
        my_user.is_superuser = False
        my_user.is_active = True
        if my_user.assignement == "Management":
            my_user.is_staff = True
        else:
            my_user.is_staff = False
        my_user.set_password(password)
        my_user.save(using=self._db)
        if assignement == "Commercial":
            commercial_group, created = Group.objects.get_or_create(name ='Commercial')
            my_user.groups.add(commercial_group)
        elif assignement == "Support":
            support_group, created = Group.objects.get_or_create(name ='Support')
            my_user.groups.add(support_group)
        elif assignement == "Management":
            management_group, created = Group.objects.get_or_create(name ='Management')
            my_user.groups.add(management_group)
        return my_user

    def create_superuser(self,
                         username,
                         first_name,
                         last_name,
                         email,
                         assignement,
                         password=None):
        my_user = self.model(username=username,
                          first_name=first_name,
                          last_name=last_name,
                          email=email,
                          assignement='Management')
        my_user.is_active = True
        my_user.is_staff = True
        my_user.is_superuser = True
        my_user.set_password(password)
        my_user.save(using=self._db)
        management_group, created = Group.objects.get_or_create(name ='Management')
        my_user.groups.add(management_group)
        return my_user


class User(AbstractUser):
    class Assignement(models.TextChoices):
        COMMERCIAL = 'Commercial'
        SUPPORT = 'Support'
        MANAGEMENT = 'Management'

    assignement = models.CharField(max_length=64, choices=Assignement.choices)
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    email = models.EmailField(max_length=256, blank=False)
    update = models.DateTimeField(null=True)

    objects = MyUserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'assignement']

    def __str__(self):
        return f"Utilisateur {self.pk}"
