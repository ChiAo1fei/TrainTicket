"""__author__ == ChiAo"""
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from user.models import User


class UserAuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 解析请求request来之后直接执行的，还没有匹配路由
        # print('process_request')
        path = request.path
        if path not in ['/user/userinfo/']:
            return None

        if 'account_number' in request.session:
            user = User.objects.filter(account_number=request.session['account_number'])
            request.user = user
            return None
        return HttpResponseRedirect(reverse('user:login'))