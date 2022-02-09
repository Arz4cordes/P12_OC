from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import ClientSerializer, ContractSerializer, EventSerializer
# Create your views here.


class ClientViewSet(ModelViewSet):
    """
    With this Class Based View, you can:
    view the list of all clients,
    create a new client,
    view one particular client,
    update one client
    or delete one client
    """
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContractViewSet(ModelViewSet):
    """
    With this Class Based View, you can:
    view the list of all contracts,
    create a new contrac,
    view one particular contract,
    update one contract
    or delete one contract
    """
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventViewSet(ModelViewSet):
    """
    With this Class Based View, you can:
    view the list of all events,
    create a new event,
    view one particular event,
    update one event
    or delete one event
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
