from django.contrib import admin
from .models import BytedeskConfig

@admin.register(BytedeskConfig)
class BytedeskConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'placement', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'placement', 'theme')
    search_fields = ('name', 'org_id', 'sid')
    fieldsets = (
        ('基本设置', {
            'fields': ('name', 'base_url', 'is_active')
        }),
        ('位置设置', {
            'fields': ('placement', 'auto_popup', 'window_width')
        }),
        ('邀请框设置', {
            'fields': ('invite_show', 'invite_text')
        }),
        ('气泡设置', {
            'fields': ('bubble_show', 'bubble_icon', 'bubble_title', 'bubble_subtitle')
        }),
        ('主题设置', {
            'fields': ('theme', 'background_color', 'text_color')
        }),
        ('客服参数', {
            'fields': ('org_id', 'type_id', 'sid')
        }),
    ) 