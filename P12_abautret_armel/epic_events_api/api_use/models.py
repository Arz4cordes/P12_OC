from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    phone1 = models.PositiveBigIntegerField
    phone2 = models.PositiveBigIntegerField
    company = models.CharField(max_length=128)
    active = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField
    # responsible: FK commercial_team


class Contract(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField
    signed = models.BooleanField(default=False)
    signature_date = models.DateTimeField
    total_amount = models.PositiveBigIntegerField
    # client: FK Client


class Event(models.Model):
    EVENT_STATUS = [
        ('UP', 'Upcoming'),
        ('DONE', 'Finished')
    ]

    date = models.DateTimeField
    status = models.CharField(max_length=64, choices=EVENT_STATUS)
    comments = models.TextField(max_length=500000)
    # responsible: FK support_team
    # contract: FK Contract

# CREER LES MODELES pour support_team, commercial_team, management_team
