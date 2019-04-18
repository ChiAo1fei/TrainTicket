from datetime import datetime

from django.shortcuts import render

# Create your views here.
from train.forms import UserInputAboutTrain
from train.models import TrainStationPrice


def selectTrainTicket(request):
    if request.method == 'GET':
        if 'account_number' in request.session:
            return render(request, 'selectTicket.html', {'session': request.session['account_number']})
        return render(request, 'selectTicket.html', {'session': None})

    if request.method == 'POST':
        # 获取用户输入的数据
        go_station = request.POST.get('go_station')
        arrive_station = request.POST.get('arrive_station')
        # leave_date = request.POST.get('leave_date')
        l_date = datetime.strptime(request.POST.get('leave_date'), '%Y-%m-%d').date()
        train_infos = TrainStationPrice.objects.filter(go_station__station_name=go_station,
                                                       arrive_station__station_name=arrive_station,
                                                       train_date=l_date).all()
        # print(info)
        # print(go_station, arrive_station, leave_date)
        return render(request, 'selectTicket.html', {'train_infos': train_infos})


def index(request):
    if request.method == 'GET':
        if 'account_number' in request.session:
            return render(request, 'index.html', {'session': request.session['account_number']})
        return render(request, 'index.html', {'session': None})

    if request.method == 'POST':

        form = UserInputAboutTrain(request.POST)
        if form.is_valid():
            l_date = datetime.strptime(form.cleaned_data['leave_date'], '%Y-%m-%d').date()
            train_infos = TrainStationPrice.objects.filter(go_station__station_name=form.cleaned_data['go_station'],
                                                           arrive_station__station_name=form.cleaned_data[
                                                               'arrive_station'],
                                                           train_date=l_date).all()
            return render(request, 'selectTicket.html', {'train_infos': train_infos})
        errors = form.errors
        return render(request, 'index.html', {'errors': errors})
