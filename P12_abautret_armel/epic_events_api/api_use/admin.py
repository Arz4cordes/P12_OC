from django.contrib import admin
from api_use.models import Client, Contract, Event
# Register your models here.


class ContractInLine(admin.TabularInline):
    model = Contract
    extra = 1


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    empty_value_display = 'No data'
    list_display = ('email', 'phone1', 'phone2', 'company', 'responsible')
    inlines = [
        ContractInLine,
    ]

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    empty_value_display = 'No data'
    list_display = ('creation_date', 'signed', 'signature_date', 'total_amount', 'client')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    empty_value_display = 'No data'
    list_display = ('date', 'status', 'responsible', 'contract')
