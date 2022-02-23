from django.contrib import admin
from api_event.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    empty_value_display = 'No data'
    list_display = ('date', 'status', 'responsible', 'contract')
