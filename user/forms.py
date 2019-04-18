"""__author__ == ChiAo"""

from django import forms

from user.models import User


class UserRegisterForm(forms.Form):
    # 定义表单，验证数据
    account_number = forms.CharField(required=True, max_length=20,
                                     error_messages={
                                         'max_length': '账号长度不可超过20位'
                                     })
    password = forms.CharField(required=True, max_length=20,
                               error_messages={
                                   'max_length': '密码长度不可超过20位'
                               })
    password2 = forms.CharField(required=True, max_length=20,
                                error_messages={
                                    'max_length': '密码长度不可超过20位'
                                })
    sex = forms.IntegerField(required=True)
    name = forms.CharField(required=True)
    id_card = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    phone = forms.CharField(required=True)
    address = forms.CharField(required=True)

    def clean(self):
        # 用于校验form表单的数据， 返回校验字段后的结果
        # 默认调用
        # 校验密码是否一致
        pwd1 = self.cleaned_data.get('password')
        pwd2 = self.cleaned_data.get('password2')

        if pwd1 and pwd2:
            if pwd1 != pwd2:
                raise forms.ValidationError({'password2': '两次密码不一致'})

        return self.cleaned_data

    def clean_account_number(self):

        # 注册校验 账号 是否存在数据库
        user = User.objects.filter(account_number=self.cleaned_data.get('account_number')).first()
        if user:
            raise forms.ValidationError('该账号已经被注册')
        return self.cleaned_data['account_number']

    def clean_id_card(self):

        if len(self.cleaned_data.get('id_card')) != 18:
            raise forms.ValidationError('身份证号码长度不正确')
        # 校验身份证号
        user = User.objects.filter(id_card=self.cleaned_data.get('id_card')).first()
        if user:
            raise forms.ValidationError('该身份证已经被注册')
        return self.cleaned_data['id_card']

    def clean_phone(self):

        if len(self.cleaned_data.get('phone')) != 11:
            raise forms.ValidationError('电话号码长度不正确')
        # 校验电话号码
        user = User.objects.filter(phone=self.cleaned_data.get('phonr')).first()
        if user:
            raise forms.ValidationError('该手机号已经被注册')
        return self.cleaned_data['phone']


class UserLoginForm(forms.Form):
    account_number = forms.CharField(required=True, max_length=20,
                                     error_messages={
                                         'max_length': '账号长度不可超过20位'
                                     })
    password = forms.CharField(required=True, max_length=20,
                               error_messages={
                                   'max_length': '密码长度不可超过20位'
                               })

    def clean(self):
        account_number = self.cleaned_data.get('account_number')
        password = self.cleaned_data.get('password')

        if account_number and password:
            user = User.objects.filter(account_number=account_number).first()
            if not user:
                raise forms.ValidationError({'account_number': '用户不存在'})
            else:
                if user.password != password:
                    raise forms.ValidationError({'password': '密码错误'})

        return self.cleaned_data


class UserUpdateForm(forms.Form):
    password = forms.CharField(required=True, max_length=20,
                               error_messages={
                                   'max_length': '密码长度不可超过20位'
                               })
    sex = forms.IntegerField(required=True)
    name = forms.CharField(required=True)
    id_card = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    phone = forms.CharField(required=True)
    address = forms.CharField(required=True)

    def clean_id_card(self):

        if len(self.cleaned_data.get('id_card')) != 18:
            raise forms.ValidationError('身份证号码长度不正确')
        # 校验身份证号
        user = User.objects.filter(id_card=self.cleaned_data.get('id_card')).first()
        if user:
            raise forms.ValidationError('该身份证已经被注册')
        return self.cleaned_data['id_card']

    def clean_phone(self):

        if len(self.cleaned_data.get('phone')) != 11:
            raise forms.ValidationError('电话号码长度不正确')
        # 校验电话号码
        user = User.objects.filter(phone=self.cleaned_data.get('phonr')).first()
        if user:
            raise forms.ValidationError('该手机号已经被注册')
        return self.cleaned_data['phone']
