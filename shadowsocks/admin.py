from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'balance', ]


class InviteCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'time_created']


class AliveipAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'ip_address', 'time']


class MoneyCodeAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'isused']


class AlipayAdmin(admin.ModelAdmin):
    list_display = ['info_code', 'amount', 'money_code', 'time', ]
    search_fields = ['info_code', ]

class AlipayRequestAdmin(admin.ModelAdmin):
    list_display = ['username', 'amount','info_code', 'time', ]


# Register your models here.
admin.site.register(models.User, UserAdmin)
admin.site.register(models.InviteCode, InviteCodeAdmin)
admin.site.register(models.Aliveip, AliveipAdmin)
admin.site.register(models.Node)
admin.site.register(models.Donate)
admin.site.register(models.MoneyCode, MoneyCodeAdmin)
admin.site.register(models.Shop)
admin.site.register(models.PurchaseHistory)
admin.site.register(models.AlipayRecord, AlipayAdmin)
admin.site.register(models.AlipayRequest,AlipayRequestAdmin)
admin.site.register(models.NodeInfoLog)
admin.site.register(models.NodeOnlineLog)

