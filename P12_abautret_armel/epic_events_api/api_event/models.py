from django.db import models
from django.conf import settings
from api_contract.models import Contract


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
