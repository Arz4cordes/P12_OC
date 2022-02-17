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


class Contract(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(null=True)
    signed = models.BooleanField(default=False)
    signature_date = models.DateTimeField(null=True)
    total_amount = models.PositiveBigIntegerField(default=0)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

    def __str__(self):
        the_client = self.client
        if the_client:
             return f"Contrat {self.pk} | Client: {the_client.first_name} {the_client.last_name}"
        else:
            return f"Contrat {self.pk} | Problème: pas de cleint associé !"

class Event(models.Model):
    EVENT_STATUS = [
        ('UP', 'Upcoming'),
        ('DONE', 'Finished')
    ]

    date = models.DateTimeField(null=True)
    status = models.CharField(max_length=64, choices=EVENT_STATUS, default='Upcoming')
    comments = models.TextField(max_length=500000, blank=True)
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE)

    def __str__(self):
        the_contract = self.contract
        the_responsible = self.responsible
        if the_contract:
            text = f"Evénement {self.pk} | Contrat {the_contract.pk} "
            text += f"| {the_responsible}"
            return text
        else:
            text = f"Evénement {self.pk} | Problème: pas de contrat associé ! "
            text += f"| {the_responsible}"
            return text
