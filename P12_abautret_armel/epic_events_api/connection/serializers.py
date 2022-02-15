from rest_framework.serializers import ModelSerializer
from connection.models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'assignement', 'date_joined']