from django.contrib import admin
from .models import Cust, Service, Product

admin.site.register(Cust)
admin.site.register(Service)
admin.site.register(Product)