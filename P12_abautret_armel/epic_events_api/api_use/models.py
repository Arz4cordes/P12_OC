from django.db import models
from django.conf import settings
# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    email = models.EmailField(max_length=256, blank=False)
    phone1 = models.PositiveBigIntegerField(default=0)
    phone2 = models.PositiveBigIntegerField(default=0)
    company = models.CharField(max_length=128, blank=True)
    active = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(null=True)
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.email}"
