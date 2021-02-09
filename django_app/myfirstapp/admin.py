from django.contrib import admin

# Register your models here.

from .models import *

class ProductionConsumedAdmin(admin.ModelAdmin):
    list_display = ('prod_report', 'consumed', 'consumed_uom', 'quantity', 'price')

admin.site.register(Nomenclature)
admin.site.register(Counterparty)
admin.site.register(UOM)
admin.site.register(ConversionRate)
admin.site.register(Purchase)
admin.site.register(Production)
admin.site.register(ProductionConsumed, ProductionConsumedAdmin)
admin.site.register(ProductionProduced)
