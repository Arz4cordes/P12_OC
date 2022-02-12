from rest_framework import serializers
from connection.models import User

class ConnectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']