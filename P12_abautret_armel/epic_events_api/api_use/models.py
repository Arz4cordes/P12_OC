from django.db import models
from django.conf import settings
# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    email = models.EmailField(max_length=256, blank=False)
    phone1 = models.PositiveBigIntegerField
    phone2 = models.PositiveBigIntegerField
    company = models.CharField(max_length=128)
    active = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Contract(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField
    signed = models.BooleanField(default=False)
    signature_date = models.DateTimeField
    total_amount = models.PositiveBigIntegerField
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)


class Event(models.Model):
    EVENT_STATUS = [
        ('UP', 'Upcoming'),
        ('DONE', 'Finished')
    ]

    date = models.DateTimeField
    status = models.CharField(max_length=64, choices=EVENT_STATUS)
    comments = models.TextField(max_length=500000)
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
