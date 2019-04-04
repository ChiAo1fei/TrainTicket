from django.shortcuts import render

# Create your views here.
# 登录

def login(request):
    if request.method == 'GET':
        return render(request, 'index.html')