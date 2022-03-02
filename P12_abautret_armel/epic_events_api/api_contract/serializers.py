from rest_framework import serializers
from api_contract.models import Contract


class ContractListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contract
        fields = ['url', 'client', 'creation_date', 'signed']


class ContractDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contract
        fields = ['pk', 'client', 'creation_date', 'update', 'signed', 'signature_date',
                  'total_amount']
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
