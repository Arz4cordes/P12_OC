from django.contrib.auth import authenticate
from rest_framework import serializers
from api_use.models import Client, Contract, Event

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['pk', 'first_name', 'last_name', 'email', 'phone1', 'phone2',
                  'company', 'creation_date', 'update', 'responsible']
        read_only_fields = ['pk']


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ['pk', 'creation_date', 'update', 'signed', 'signature_date',
                  'total_amount', 'client']
        read_only_fields = ['pk']

    def validate(self, data):
        the_responsible = data['client'].responsible
        current_user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            current_user = request.user
        if current_user == the_responsible:
            return data
        else:
            text = 'Vous devez être un responsable du client sélectionné'
            raise serializers.ValidationError(text)


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['pk', 'date', 'status', 'comments', 'responsible', 'contract']
        read_only_fields = ['pk', 'status', 'responsible']
    
    def validate(self, data):
        is_it_signed = data['contract'].signed
        responsible_for_client = data['contract'].client.responsible
        current_user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            current_user = request.user
        if not is_it_signed:
            text = 'Le contrat doit être signé avant de créer un événement'
            raise serializers.ValidationError(text)
        elif current_user != responsible_for_client:
            text = 'Vous devez être un responsable du client'
            text += ' correspondant au contrat sélectionné'
            raise serializers.ValidationError(text)
        else:
            return data
 
