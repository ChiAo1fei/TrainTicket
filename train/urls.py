"""__author__ == ChiAo"""


from django.urls import path, include
from train.views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('selectTrainTicket/', selectTrainTicket, name='selectTrainTicket'),
]