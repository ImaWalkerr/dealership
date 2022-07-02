from django.urls import path, include
from .views import CustomerViewSet, CustomerCarViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'customer_offer', CustomerCarViewSet, basename='customer_offer')

urlpatterns = [
    path('customer/', include(router.urls)),
]
