from django.db import models

# Create your models here.


class Order(models.Model):
    """
        定义订单模型
    """
    # 订单号
    order_id = models.CharField(verbose_name='订单号', max_length=64, null=True, unique=True)
    # 账号
    account_num = models.IntegerField(verbose_name='账号', null=True)
    # 姓名
    name = models.CharField(verbose_name='姓名', max_length=10, null=True)
    # 证件号
    id_card = models.CharField(verbose_name='证件号', null=True, unique=True, max_length=18)
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
    order_time = models.CharField(verbose_name='订票日期', max_length=64, null=True)
    # 状态
    STATUS = (
        (1, '已支付'),
        (2, '已改签'),
        (3, '已退票'),
    )
    status = models.IntegerField(choices=STATUS, verbose_name='状态', null=True)

    class Meta:
        db_table = 'order'
        verbose_name_plural = '订单信息'
        verbose_name = '订单信息'
