from django.shortcuts import get_object_or_404
from rest_framework import serializers
from api_event.models import Event
from api_contract.models import Contract


class EventListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['url', 'date', 'status', 'contract']
        read_only_fields = ['pk', 'status', 'responsible']


class EventDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['pk', 'responsible', 'date', 'status', 'comments', 'contract']
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

    def to_representation(self, instance):
        result = super(EventDetailSerializer, self).to_representation(instance)
        associated_contract = result['contract']
        the_contract = get_object_or_404(Contract, pk=associated_contract)
        if the_contract:
            associated_client = the_contract.client.pk
            result['client'] = associated_client
        return result
