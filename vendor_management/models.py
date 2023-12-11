from django.db import models
from django.db.models import Count, Avg, Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.name
    
    def calculate_on_time_delivery_rate(self):
        completed_pos = PurchaseOrder.objects.filter(
            vendor=self,
            status='completed',
            delivery_date__lte=timezone.now()
        ).count()

        total_completed_pos = PurchaseOrder.objects.filter(
            vendor=self,
            status='completed'
        ).count()

        return completed_pos / total_completed_pos if total_completed_pos > 0 else 0

    def calculate_quality_rating_avg(self):
        completed_pos = PurchaseOrder.objects.filter(
            vendor=self,
            status='completed',
            quality_rating__isnull=False
        )
        return completed_pos.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0

    def calculate_average_response_time(self):
        completed_pos = PurchaseOrder.objects.filter(
            vendor=self,
            acknowledgment_date__isnull=False
        )
        response_times = [(po.acknowledgment_date - po.issue_date).total_seconds()
                          for po in completed_pos]

        return sum(response_times) / len(response_times) if len(response_times) > 0 else 0

    def calculate_fulfillment_rate(self):
        successful_pos = PurchaseOrder.objects.filter(
            vendor=self,
            status='completed',
            issue_date__isnull=True 
        ).count()

        total_pos = PurchaseOrder.objects.filter(
            vendor=self,
        ).count()

        return successful_pos / total_pos if total_pos > 0 else 0

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number
    
    
    def calculate_on_time_delivery_rate(self):
        completed_pos = PurchaseOrder.objects.filter(
            vendor=self.vendor,
            status='completed',
            delivery_date__lte=timezone.now()
        ).count()

        total_completed_pos = PurchaseOrder.objects.filter(
            vendor=self.vendor,
            status='completed'
        ).count()

        return completed_pos / total_completed_pos if total_completed_pos > 0 else 0

    def calculate_quality_rating_avg(self):
        completed_pos = PurchaseOrder.objects.filter(
            vendor=self.vendor,
            status='completed',
            quality_rating__isnull=False
        )
        return completed_pos.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0

    def calculate_average_response_time(self):
        completed_pos = PurchaseOrder.objects.filter(
            vendor=self.vendor,
            acknowledgment_date__isnull=False
        )
        response_times = [(po.acknowledgment_date - po.issue_date).total_seconds()
                          for po in completed_pos]

        return sum(response_times) / len(response_times) if len(response_times) > 0 else 0

    def calculate_fulfillment_rate(self):
        successful_pos = PurchaseOrder.objects.filter(
            vendor=self.vendor,
            status='completed',
            issue_date__isnull=True 
        ).count()

        total_pos = PurchaseOrder.objects.filter(
            vendor=self.vendor,
        ).count()

        return successful_pos / total_pos if total_pos > 0 else 0
    
    
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
    
