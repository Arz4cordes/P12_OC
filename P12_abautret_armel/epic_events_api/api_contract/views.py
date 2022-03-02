from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from api_contract.serializers import ContractListSerializer, ContractDetailSerializer

from api_contract.models import Contract
from api_contract.permissions import CanViewContracts


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
