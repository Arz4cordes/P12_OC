from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from connection.models import User
from connection.serializers import UserSerializer
# Create your views here.


class HomeAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        actual_user = User.objects.get(username=request.user.username)
        serializer = UserSerializer(actual_user)
        return Response(serializer.data)
