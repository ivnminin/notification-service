from django.contrib import admin

from . import models


class ClientAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'number', 'code', 'tag', 'gmt')

    class Meta:
        model = models.Client


class MessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'updated_at')

    class Meta:
        model = models.Message


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'message', 'time_start', 'time_end')

    class Meta:
        model = models.Delivery


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('status', 'client', 'delivery')

    class Meta:
        model = models.Membership


admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Message, MessageAdmin)
admin.site.register(models.Delivery, DeliveryAdmin)
admin.site.register(models.Membership, MembershipAdmin)
