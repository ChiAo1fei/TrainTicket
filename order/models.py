from django.db import models

# Create your models here.


class Order(models.Model):
    """
        定义订单模型
    """
    # 订单号
    order_id = models.CharField(verbose_name='订单号', max_length=20, null=True, unique=True)
    # 账号
    account_num = models.IntegerField(verbose_name='账号', null=True)
    # 姓名
    name = models.CharField(verbose_name='姓名', max_length=10, null=True)
    # 证件号
    id_card = models.IntegerField(verbose_name='证件号', null=True)
    # 出发地址
    go_station = models.CharField(verbose_name='出发地址', max_length=10, null=True)
    # 出发时间
    go_time = models.CharField(verbose_name='出发时间', max_length=10, null=True)
    # 到达地址
    arrive_station = models.CharField(verbose_name='到达地址', max_length=10, null=True)
    # 到达时间
    arrive_time = models.CharField(verbose_name='到达时间', max_length=10, null=True)
    # 座位级别
    seat_level = models.CharField(verbose_name='座位级别', max_length=10, null=True)
    # 票价
    seat_price = models.CharField(verbose_name='票价', max_length=10, null=True)
    # 订票日期
    order_time = models.DateTimeField(verbose_name='订票日期', auto_now_add=True)
    # 是否退票
    IS_DELETE = (
        ('0', '否'),
        ('1', '是')
    )
    is_delete = models.IntegerField(choices=IS_DELETE, verbose_name='是否退票', default=0)
    # 是否改签
    IS_ALTER = (
        ('0', '否'),
        ('1', '是')
    )
    is_alter = models.IntegerField(choices=IS_ALTER, verbose_name='是否改签', default=0)

    class Meta:
        db_table = 'order'
        verbose_name_plural = '订单信息'
        verbose_name = '订单信息'
