from django.contrib import admin
from .models import *


def approve(modeladmin, request, queryset):
    queryset.update(approve=True)


def reject(modeladmin, request, queryset):
    queryset.update(approve=False)


approve.short_description = 'Approve selected ads'
reject.short_description = 'Reject selected ads'


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ('approve',)
    list_display = ('title', 'approve')
    actions = [approve, reject]


admin.site.register(Advertiser)
