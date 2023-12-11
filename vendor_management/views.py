from rest_framework import generics
from rest_framework.response import Response
from .models import Vendor, PurchaseOrder,HistoricalPerformance
from .serializers import VendorSerializer,PurchaseOrderSerializer
from rest_framework.permissions import IsAuthenticated

class VendorListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_url_kwarg = 'vendor_id'


# class VendorPerformanceRetrieveView(generics.RetrieveAPIView):
#     queryset = HistoricalPerformance.objects.all()
#     serializer_class = VendorSerializer
#     lookup_url_kwarg = 'vendor_id'

#     def retrieve(self, request, *args, **kwargs):
#         vendor = self.get_object().vendor

#         on_time_delivery_rate = vendor.on_time_delivery_rate
#         quality_rating_avg = vendor.quality_rating_avg
#         average_response_time = vendor.average_response_time
#         fulfillment_rate = vendor.fulfillment_rate

#         data = {
#             'on_time_delivery_rate': on_time_delivery_rate,
#             'quality_rating_avg': quality_rating_avg,
#             'average_response_time': average_response_time,
#             'fulfillment_rate': fulfillment_rate,
#         }

#         return Response(data)
    
    
class VendorPerformanceRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_url_kwarg = 'vendor_id'

    def retrieve(self, request, *args, **kwargs):
        vendor = self.get_object()

        on_time_delivery_rate = vendor.calculate_on_time_delivery_rate()
        quality_rating_avg = vendor.calculate_quality_rating_avg()
        average_response_time = vendor.calculate_average_response_time()
        fulfillment_rate = vendor.calculate_fulfillment_rate()

        data = {
            'on_time_delivery_rate': on_time_delivery_rate,
            'quality_rating_avg': quality_rating_avg,
            'average_response_time': average_response_time,
            'fulfillment_rate': fulfillment_rate,
        }

        return Response(data)    

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_url_kwarg = 'po_id'
    
    
class PurchaseOrderAcknowledgeView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_url_kwarg = 'po_id'

    def perform_update(self, serializer):
        serializer.save(acknowledgment_date=timezone.now())    