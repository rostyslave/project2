from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('register/', views.register, name='register'),

    path('devices/', views.device_list, name='device_list'),
    path('devices/create/', views.device_create, name='device_create'),
    path('devices/<int:device_id>/edit/', views.device_edit, name='device_edit'),
    path('repairs/', views.repair_list, name='repair_list'),
    path('repairs/create/', views.repair_create, name='repair_create'),
    path('repairs/<int:repair_id>/', views.repair_detail, name='repair_detail'),
]
