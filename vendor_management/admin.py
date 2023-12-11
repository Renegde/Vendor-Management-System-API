from django.contrib import admin
from .models import Vendor, PurchaseOrder, HistoricalPerformance

# Register your models with the admin site
admin.site.register(Vendor)
admin.site.register(PurchaseOrder)
admin.site.register(HistoricalPerformance)

