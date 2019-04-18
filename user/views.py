from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
# 登录
from django.urls import reverse

from user.forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from user.models import User


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            request.session['account_number'] = form.cleaned_data['account_number']
            return HttpResponseRedirect(reverse('train:index'))
        errors = form.errors
        return render(request, 'login.html', {'errors': errors})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        # 定义表单验证页面传递的参数
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # 校验成功
            user = User()
            user.account_number = form.cleaned_data['account_number']
            user.password = form.cleaned_data['password']
            user.name = form.cleaned_data['name']
            user.sex = form.cleaned_data['sex']
            user.id_card = form.cleaned_data['id_card']
            user.age = form.cleaned_data['age']
            user.phone = form.cleaned_data['phone']
            user.address = form.cleaned_data['address']
            user.save()
            success = '注册成功'
            return render(request, 'register.html', {'success': success})
        errors = form.errors
        return render(request, 'register.html', {'errors': errors})


def userinfo(request):
    if request.method == 'GET':
        if 'account_number' in request.session:
            user = User.objects.filter(account_number=request.session['account_number']).first()
            return render(request, 'user.html', {'userInfo': user, 'session': request.session['account_number']})

    if request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(account_number=request.session['account_number']).first()
            user.password = form.cleaned_data['password']
            user.name = form.cleaned_data['name']
            user.sex = form.cleaned_data['sex']
            user.id_card = form.cleaned_data['id_card']
            user.age = form.cleaned_data['age']
            user.phone = form.cleaned_data['phone']
            user.address = form.cleaned_data['address']
            user.save()
            success = '修改成功'
            return render(request, 'user.html', {'success': success, 'userInfo': user})
        errors = form.errors
        return render(request, 'user.html', {'errors': errors})


def logout(request):
    if request.method =='GET':
        request.session['account_number'] = None
        return render(request, 'index.html')
