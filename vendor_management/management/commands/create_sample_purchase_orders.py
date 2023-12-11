from django.core.management.base import BaseCommand
from vendor_management.models import PurchaseOrder, Vendor

class Command(BaseCommand):
    help = 'Create sample purchase orders'

    def handle(self, *args, **options):
        vendor_a = Vendor.objects.get(vendor_code='A123')
        vendor_b = Vendor.objects.get(vendor_code='B456')

        PurchaseOrder.objects.create(vendor=vendor_a, po_number='POA001', order_date='2023-01-01', delivery_date='2023-01-10', items={'item': 'Product A'}, quantity=100, status='completed', quality_rating=4.0, issue_date='2023-01-02', acknowledgment_date='2023-01-03')
        PurchaseOrder.objects.create(vendor=vendor_b, po_number='POB001', order_date='2023-02-01', delivery_date='2023-02-10', items={'item': 'Product B'}, quantity=150, status='completed', quality_rating=4.5, issue_date='2023-02-02', acknowledgment_date='2023-02-03')

        self.stdout.write(self.style.SUCCESS('Sample purchase orders created successfully.'))
