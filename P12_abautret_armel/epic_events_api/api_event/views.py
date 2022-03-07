from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from api_event.serializers import EventListSerializer, EventDetailSerializer, EventUpdateSerializer

from api_event.models import Event
from api_event.permissions import CanViewEvents


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
    update_serializer_class = EventUpdateSerializer
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
        if self.request.method == 'PUT':
            return self.update_serializer_class
        elif self.action == 'retrieve' or self.request.method == 'POST':
            return self.detail_serializer_class
        return super().get_serializer_class()
