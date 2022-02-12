from rest_framework import serializers
from api_use.models import Client, Contract, Event

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone1', 'phone2',
                  'company', 'creation_date', 'update', 'responsible']


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ['creation_date', 'update', 'signed', 'signature_date',
                  'total_amount', 'client']


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['date', 'status', 'comments', 'responsible_email', 'contract']
