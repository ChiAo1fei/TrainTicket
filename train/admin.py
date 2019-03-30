import xadmin
from .models import *


class StationAdmin(object):
    list_display = ('station_firstLetter', 'station_name', 'station_code')


class TrainInfoAdmin(object):
    list_display = ('train_date', 'train_type', 'train_num', 'origin_station', 'go_time', 'destination_station',
                    'arrive_time', 'running_time', 'is_morrow', 'is_delete')


class TrainStationPriceAdmin(object):
    list_display = ('train_id', 'go_station', 'go_time', 'arrive_station', 'arrive_time', 'no_seat_nums',
                    'no_seat_price', 'hard_seat_nums', 'hard_seat_price', 'hard_berth_nums', 'hard_berth_price',
                    'second_seat_nums', 'second_seat_price', 'first_seat_nums', 'first_seat_price', 'business_seat_nums'
                    , 'business_seat_price')


xadmin.site.register(Station, StationAdmin)
xadmin.site.register(TrainInfo, TrainInfoAdmin)
xadmin.site.register(TrainStationPrice, TrainStationPriceAdmin)