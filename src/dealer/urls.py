from django.urls import path, include
from .views import DealerViewSet, DealerGeneralViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'dealer', DealerViewSet, basename='dealer')
router.register(r'dealer_general', DealerGeneralViewSet, basename='dealer_general')

urlpatterns = [
    path('dealer/', include(router.urls)),
]
