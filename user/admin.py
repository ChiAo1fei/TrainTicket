import xadmin
from .models import *


class UserAdmin(object):
    list_display = ('account_number', 'password', 'name', 'sex', 'id_card', 'age', 'phone', 'address')


xadmin.site.register(User, UserAdmin)