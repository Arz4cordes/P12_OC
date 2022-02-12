from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from connection.serializers import ConnectionSerializer
# Create your views here.


class ConnectionView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ConnectionSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data['username']
            password = request.data['password']
            the_user = authenticate(request, username=username, password=password)
            if the_user is not None:
                login(request, the_user)
                user_connected = request.user
                u_name = user_connected.username
                first_name = user_connected.first_name
                last_name = user_connected.last_name
                data = {'Prénom: ': first_name,
                        'Nom: ' : last_name,
                        'Username: ': u_name,
                        'Statut: ' : 'Connecté'}
                return Response(data)
            else:
                data = {
                    'Statut: ': 'Identifiants invalides'
                }
                return Response(data)
        else:
            return HttpResponse('Formulaire non valide')
