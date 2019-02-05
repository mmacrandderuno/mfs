from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    url('registration/', include('django.contrib.auth.urls')),
    path('customer/', views.cust_list, name='cust_list'),
    path('deleted_customers/', views.deleted_customers, name='deleted_customers'),
    path('customer/<int:pk>/', views.cust_detail, name='cust_detail'),
    path('customer/new/', views.cust_new, name='cust_new'),
    path('customer/<int:pk>/edit/', views.cust_edit, name='cust_edit'),
    path('customer/<int:custid>/orders/', views.orders, name='orders'),
    path('customer/<int:custid>/deletedorders/', views.deletedorders, name='deletedorders'),
    path('products/<int:pk>/', views.prod_detail, name='prod_detail'),
    path('customer/<int:custid>/products/new/', views.prod_new, name='prod_new'),
    path('products/<int:pk>/edit/', views.prod_edit, name='prod_edit'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('customer/<int:custid>/services/new/', views.service_new, name='service_new'),
    path('services/<int:pk>/edit/', views.service_edit, name='service_edit'),
]
