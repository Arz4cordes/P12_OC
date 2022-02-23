from django.contrib import admin
from api_contract.models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    empty_value_display = 'No data'
    list_display = ('creation_date', 'signed', 'signature_date', 'total_amount', 'client')
