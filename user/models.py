from django.db import models

# Create your models here.
# 定义用户信息模型


class User(models.Model):
    """
        定义普通用户
    """
    # 用户账号
    account_number = models.CharField(verbose_name='账号', max_length=20, unique=True, null=True)
    # 用户密码
    password = models.CharField(verbose_name='密码', max_length=20, null=True)
    # 姓名
    name = models.CharField(verbose_name='姓名', max_length=10, null=True)
    # 性别
    SEX = (
        (0, '男'),
        (1, '女')
    )
    sex = models.IntegerField(choices=SEX, verbose_name='性别', default=0)
    # 证件号
    id_card = models.CharField(verbose_name='证件号', null=True, unique=True, max_length=18)
    # 年龄
    age = models.IntegerField(verbose_name='年龄')
    # 电话
    phone = models.CharField(verbose_name='电话', unique=True, null=True, max_length=11)
    # 地址
    address = models.CharField(verbose_name='地址', max_length=255)

    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
