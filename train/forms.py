"""__author__ == ChiAo"""

from django import forms


class UserInputAboutTrain(forms.Form):
    leave_date = forms.CharField(required=True,
                                 error_messages={
                                     'required': '请输入日期'
                                 })
    go_station = forms.CharField(required=True,
                                 error_messages={
                                     'required': "请输入出发地址"
                                 })
    arrive_station = forms.CharField(required=True,
                                     error_messages={
                                         'required': "请输入到达地址"
                                     })