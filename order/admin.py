import xadmin

from .models import *


class OrderAdmin(object):
    list_display = ('order_id', 'account_num', 'name', 'id_card', 'go_station', 'go_time', 'arrive_station',
                    'arrive_time', 'seat_level', 'seat_price', 'order_time', 'is_delete', 'is_alter')


xadmin.site.register(Order, OrderAdmin)
