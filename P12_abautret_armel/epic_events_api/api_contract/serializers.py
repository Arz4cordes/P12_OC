from rest_framework import serializers
from api_contract.models import Contract

class ContractListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ['pk', 'creation_date', 'signed', 'client']
        read_only_fields = ['pk']


class ContractDetailSerializer(serializers.ModelSerializer):

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
