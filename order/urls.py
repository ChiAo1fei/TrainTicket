"""__author__ == ChiAo"""
from django.urls import path, include
from order.views import *

urlpatterns = [
    path('orderinfo/<int:id>/', orderinfo, name='orderinfo'),
    path('user_order/', user_order, name='user_order')
]