from django.db import models

# Create your models here.
#  定义火车信息模型


class Station(models.Model):
    """
        定义Station的模型
    """

    # 车站首字母
    station_firstLetter = models.CharField(verbose_name='车站首字母', max_length=10, null=True)
    # 车站名字
    station_name = models.CharField(verbose_name='站点名称', max_length=10, null=True, unique=True)
    # 车站代号
    station_code = models.CharField(verbose_name='车站代号',max_length=10, null=True, unique=True)

    class Meta:
        db_table = 'station'
        verbose_name = '站点信息'
        verbose_name_plural = '站点信息'

    def __str__(self):
        return self.station_name


class TrainInfo(models.Model):
    """
    定义TrainInfo模型
    """

    # 运行日期
    train_date = models.DateField(verbose_name='运行日期', null=True)
    # 火车类型
    TRAIN_TYPE = (
        ('C', '城际列车 C'),
        ('D', '动车组 D'),
        ('G', '高速列车 G'),
        ('Z', '直达列车 Z'),
        ('T', '特快列车 T'),
        ('K', '快速列车 K'),
        ('L', '临时旅客列车 L'),
        ('A', '局管内临时旅客列车 A'),
        ('Y', '旅游列车 Y')
    )
    train_type = models.CharField(choices=TRAIN_TYPE, verbose_name='火车类型', max_length=1, null=True)
    # 火车编号
    train_num = models.IntegerField(verbose_name='火车编号', null=True)
    # 起点站
    origin_station = models.ForeignKey(Station, verbose_name='起点站', related_name='origin_train_info', on_delete=models.CASCADE, null=True)
    # 出发时间
    go_time = models.TimeField(verbose_name='出发时间', null=True)
    # 终点站
    destination_station = models.ForeignKey(Station, verbose_name='终点站', related_name='destination_train_info', on_delete=models.CASCADE, null=True)
    # 到达日期
    arrive_time = models.TimeField(verbose_name='到达时间', null=True)
    # 运行时长
    running_time = models.CharField(verbose_name='运行时长', max_length=10, null=True)
    # 是否次日
    IS_MORROW = (
        ('1', '是'),
        ('0', '否')
    )
    is_morrow = models.CharField(choices=IS_MORROW, verbose_name='是否次日', max_length=1, default=0)
    # 是否删除
    IS_DELETE = (
        ('1', '是'),
        ('0', '否')
    )
    is_delete = models.CharField(choices=IS_DELETE, verbose_name='是否删除', max_length=1, default=0)

    class Meta:
        db_table = 'train_info'
        verbose_name_plural = '火车信息'
        verbose_name = '火车信息'

    def __str__(self):
        return str(self.train_type) + str(self.train_num)


class TrainStationPrice(models.Model):
    """
    定义火车的票价，每站到每站的票价
    TrainStationPrice.objects.filter(go_station__station_name='')
    """
    # 火车车次
    train_id = models.ForeignKey(TrainInfo, verbose_name='车次', related_name='train_price', on_delete=models.CASCADE, null=True)
    # 运行日期
    train_date = models.DateField(verbose_name='运行日期', null=True)
    # 出发站
    go_station = models.ForeignKey(Station, verbose_name='出发站', related_name='go_train_price', on_delete=models.CASCADE, null=True)
    # 出发时间
    go_time = models.TimeField(verbose_name='出发时间', null=True)
    # 到达站
    arrive_station = models.ForeignKey(Station, verbose_name='到达站', related_name='arrive_train_price', on_delete=models.CASCADE, null=True)
    # 到达时间
    arrive_time = models.TimeField(verbose_name='到达时间', null=True)
    # 无座票数
    no_seat_nums = models.IntegerField(verbose_name='无座票数', default=50)
    # 无座价格
    no_seat_price = models.DecimalField(verbose_name='价格', max_digits=4, decimal_places=1, null=True)

    # 硬座票数
    hard_seat_nums = models.IntegerField(verbose_name='硬座票数', default=50)
    # 硬座价格
    hard_seat_price = models.DecimalField(verbose_name='价格',max_digits=4, decimal_places=1, null=True)

    # 硬卧票数
    hard_berth_nums = models.IntegerField(verbose_name='硬卧票数', default=50)
    # 硬卧价格
    hard_berth_price = models.DecimalField(verbose_name='价格', max_digits=4, decimal_places=1, null=True)

    # 二等座票数
    second_seat_nums = models.IntegerField(verbose_name='二等座票数', default=50)
    #
    # 二等座价格
    second_seat_price = models.DecimalField(verbose_name='价格', max_digits=4, decimal_places=1, null=True)

    # 一等座票数
    first_seat_nums = models.IntegerField(verbose_name='一等座票数', default=50)
    # 一等座价格
    first_seat_price = models.DecimalField(verbose_name='价格', max_digits=4, decimal_places=1, null=True)

    # 商务座票数
    business_seat_nums = models.IntegerField(verbose_name='商务座票数', default=50)
    # 商务座价格
    business_seat_price = models.DecimalField(verbose_name='价格', max_digits=4, decimal_places=1, null=True)

    class Meta:
        db_table = 'train_price'
        verbose_name = '火车票价'
        verbose_name_plural = '火车票价'

