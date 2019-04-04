from __future__ import absolute_import
import xadmin
from .models import UserSettings, Log
from xadmin.layout import *

from django.utils.translation import ugettext_lazy as _, ugettext
from xadmin.views.website import LoginView
from xadmin.views import CommAdminView


class UserSettingsAdmin(object):
    model_icon = 'fa fa-cog'
    hidden_menu = True


xadmin.site.register(UserSettings, UserSettingsAdmin)


class LogAdmin(object):

    def link(self, instance):
        if instance.content_type and instance.object_id and instance.action_flag != 'delete':
            admin_url = self.get_admin_url('%s_%s_change' % (instance.content_type.app_label, instance.content_type.model), 
                instance.object_id)
            return "<a href='%s'>%s</a>" % (admin_url, _('Admin Object'))
        else:
            return ''
    link.short_description = ""
    link.allow_tags = True
    link.is_column = False

    list_display = ('action_time', 'user', 'ip_addr', '__str__', 'link')
    list_filter = ['user', 'action_time']
    search_fields = ['ip_addr', 'message']
    model_icon = 'fa fa-cog'


xadmin.site.register(Log, LogAdmin)


class LoginViewAdmin(LoginView):
    title = '火车订票管理系统'


xadmin.site.register(LoginView, LoginViewAdmin)


class GlobalSetting(CommAdminView):
    # 左上角标题
    site_title = '火车订票管理后台'
    # 页脚
    site_footer = 'Copyright © 2019 赵一飞的毕业设计'
    # menu_style = 'accordion'


xadmin.site.register(CommAdminView, GlobalSetting)