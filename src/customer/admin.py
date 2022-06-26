from django.contrib import admin

from customer.models import *


admin.site.register(Customer)
admin.site.register(CustomerHistory)
admin.site.register(Offer)
