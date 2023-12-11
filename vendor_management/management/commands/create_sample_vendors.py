from django.core.management.base import BaseCommand
from vendor_management.models import Vendor

class Command(BaseCommand):
    help = 'Create sample vendors'

    def handle(self, *args, **options):
        Vendor.objects.create(name='Vendor A', contact_details='Contact A', address='Address A', vendor_code='A123', on_time_delivery_rate=0.8, quality_rating_avg=4.2, average_response_time=2.5, fulfillment_rate=0.9)
        Vendor.objects.create(name='Vendor B', contact_details='Contact B', address='Address B', vendor_code='B456', on_time_delivery_rate=0.9, quality_rating_avg=4.5, average_response_time=1.8, fulfillment_rate=0.95)

        self.stdout.write(self.style.SUCCESS('Sample vendors created successfully.'))
