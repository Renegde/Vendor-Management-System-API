from django.urls import path
from .views import (VendorListCreateView, VendorRetrieveUpdateDestroyView,VendorPerformanceRetrieveView,
                    PurchaseOrderListCreateView,PurchaseOrderRetrieveUpdateDestroyView,PurchaseOrderAcknowledgeView)

urlpatterns = [
    path('api/vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:vendor_id>/', VendorRetrieveUpdateDestroyView.as_view(), name='vendor-retrieve-update-destroy'),
    path('api/vendors/<int:vendor_id>/performance/', VendorPerformanceRetrieveView.as_view(), name='vendor-performance-retrieve'),
    path('api/purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:po_id>/', PurchaseOrderRetrieveUpdateDestroyView.as_view(), name='purchase-order-retrieve-update-destroy'),
    path('api/purchase_orders/<int:po_id>/acknowledge/', PurchaseOrderAcknowledgeView.as_view(), name='purchase-order-acknowledge'),
    ]
