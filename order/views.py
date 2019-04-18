import time
import uuid

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from order.models import Order
from train.models import TrainStationPrice
from user.models import User


def orderinfo(request, id):
    if request.method == 'GET':
        if 'account_number' in request.session:
            train_info = TrainStationPrice.objects.get(pk=id)
            user = User.objects.filter(account_number=request.session['account_number']).first()
            return render(request, 'orderInfo.html', {'train_info': train_info, 'session': request.session['account_number'], 'user': user})

    if request.method == 'POST':

        seat = request.POST.get('selectBox')
        train_info = TrainStationPrice.objects.get(pk=id)
        user = User.objects.filter(account_number=request.session['account_number']).first()

        order = Order()
        order.order_id = uuid.uuid4().hex
        order.account_num = user.account_number
        order.name = user.name
        order.id_card = user.id_card
        order.go_station = train_info.go_station
        order.go_time = train_info.go_time
        order.arrive_station = train_info.arrive_station
        order.arrive_time = train_info.arrive_time
        order.seat_level = seat.split('￥')[0]
        order.seat_price = seat.split('￥')[1]
        order.order_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        order.status = 1
        order.save()

        return HttpResponseRedirect(reverse('order:user_order'))


def user_order(request):
    if request.method == 'GET':
        if 'account_number' in request.session:
            user = User.objects.filter(account_number=request.session['account_number']).first()
            orders = Order.objects.filter(id_card=user.id_card, status__in=[1, 2]).all()
            return render(request, 'order.html', {'session': request.session['account_number'], 'orders': orders})

    if request.method == 'POST':
        if 'ticketChange' in request.POST:
            pass

        if 'ticketRefund' in request.POST:
            orderID = request.POST['ticketRefund']
            order = Order.objects.filter(order_id=orderID).first()
            order.status = 3
            order.save()
            return HttpResponseRedirect(reverse('order:user_order'))