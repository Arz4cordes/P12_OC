from rest_framework import serializers
from api_use.models import Client

class ClientListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['pk', 'url', 'first_name', 'last_name', 'email',
                  'company']
        read_only_fields = ['pk']


class ClientDetailSerializer(serializers.ModelSerializer):
    contracts = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='contract-detail')

    class Meta:
        model = Client
        fields = ['pk', 'first_name', 'last_name', 'email', 'phone1', 'phone2',
                  'company', 'creation_date', 'update', 'responsible', 'contracts']
        read_only_fields = ['pk']
