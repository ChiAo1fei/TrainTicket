"""__author__ == ChiAo"""

from django.urls import path, include
from user.views import *

urlpatterns = [
    path('login/', login, name='login')
]