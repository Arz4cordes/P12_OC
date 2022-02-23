from django.contrib import admin
from api_use.models import Client
from api_contract.models import Contract


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
