from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Nomenclature)
admin.site.register(Counterparty)
admin.site.register(UOM)
admin.site.register(ConversionRate)
admin.site.register(Purchase)
admin.site.register(Production)
admin.site.register(ProductionConsumed)
admin.site.register(ProductionProduced)