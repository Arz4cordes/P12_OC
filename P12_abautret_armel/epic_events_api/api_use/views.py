from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.response import Response
from api_use.serializers import ClientListSerializer, \
                                ClientDetailSerializer, \
                                ContractListSerializer, \
                                ContractDetailSerializer, \
                                EventListSerializer, \
                                EventDetailSerializer
                             
from api_use.models import Client, Contract, Event
from api_use.permissions import CanViewClients, CanViewContracts, CanViewEvents
# Create your views here.

"""
    With this Class Based View, you can:
    view the list of all clients,
    create a new client,
    view one particular client,
    update one client
    or delete one client
    """
class ClientViewSet(ModelViewSet):

    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer
    permission_classes = [permissions.IsAuthenticated,
                          CanViewClients,
                          ]
    filterset_fields = ['first_name', 'last_name', 'email']
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        return Client.objects.all()

    def get_serializer_class(self):
        changes_methods = ['POST', 'PUT']
        if self.action == 'retrieve' or self.request.method in changes_methods:
            return self.detail_serializer_class
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data['responsible'] = request.user.pk
        request.POST._mutable = False
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data['responsible'] = request.user.pk
        request.POST._mutable = False
        return super(ClientViewSet, self).update(request, *args, **kwargs)


"""
    With this Class Based View, you can:
    view the list of all contracts,
    create a new contract,
    view one particular contract,
    update one contract
    or delete one contract
    """
class ContractViewSet(ModelViewSet):
    
    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer
    permission_classes = [permissions.IsAuthenticated,
                          CanViewContracts,
                          ]
    filterset_fields = ['client__first_name', 'client__last_name', 'client__email',
                        'creation_date', 'total_amount']

    def get_queryset(self):
        return Contract.objects.all()

    def get_serializer_class(self):
        changes_methods = ['POST', 'PUT']
        if self.action == 'retrieve' or self.request.method in changes_methods:
            return self.detail_serializer_class
        return super().get_serializer_class()


"""
    With this Class Based View, you can:
    view the list of all events,
    create a new event,
    view one particular event,
    update one event
    or delete one event
    """
class EventViewSet(ModelViewSet):
    
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer
    permission_classes = [permissions.IsAuthenticated,
                          CanViewEvents,
                          ]
    filterset_fields = ['contract__client__first_name',
                        'contract__client__last_name',
                        'contract__client__email',
                        'date']

    def get_queryset(self):
        return Event.objects.all()

    def get_serializer_class(self):
        changes_methods = ['POST', 'PUT']
        if self.action == 'retrieve' or self.request.method in changes_methods:
            return self.detail_serializer_class
        return super().get_serializer_class()
