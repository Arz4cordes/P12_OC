from rest_framework import serializers
from api_event.models import Event

class EventListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['pk', 'date', 'status', 'contract']
        read_only_fields = ['pk', 'status', 'responsible']


class EventDetailSerializer(serializers.ModelSerializer):

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
