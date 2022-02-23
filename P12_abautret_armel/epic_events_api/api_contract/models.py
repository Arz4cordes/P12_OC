from django.db import models
from api_use.models import Client

# Create your models here.

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
