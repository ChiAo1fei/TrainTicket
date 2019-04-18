"""__author__ == ChiAo"""

from django.urls import path, include
from user.views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('userinfo/', userinfo, name='userinfo'),
    path('logout/', logout, name='logout')
]