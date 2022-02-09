from rest_framework import serializers
from .models import Client, Contract, Event

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['firt_name', 'last_name', 'email', 'phone1', 'phone2',
                  'company', 'creation_date', 'update', 'responsible_email']


class ContractViewSet(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ['creation_date', 'update', 'signed', 'signature_date',
                  'total_amount', 'client']


class EventViewSet(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['date', 'status', 'comments', 'responsible_email', 'contract']
