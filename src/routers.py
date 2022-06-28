from rest_framework import routers

from car_dealership.urls import router as dealership_router
from customer.urls import router as customer_router
from dealer.urls import router as dealer_router


router = routers.DefaultRouter()
router.registry.extend(dealership_router.registry)
router.registry.extend(customer_router.registry)
router.registry.extend(dealer_router.registry)
