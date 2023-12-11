from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder, HistoricalPerformance

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_metrics(sender, instance, **kwargs):
    vendor = instance.vendor

    # Update metrics in real-time
    vendor.on_time_delivery_rate = vendor.calculate_on_time_delivery_rate()
    vendor.quality_rating_avg = vendor.calculate_quality_rating_avg()
    vendor.average_response_time = vendor.calculate_average_response_time()
    vendor.fulfillment_rate = vendor.calculate_fulfillment_rate()

    vendor.save()