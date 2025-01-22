from django.db import models

class BytedeskConfig(models.Model):
    name = models.CharField(max_length=100, unique=True)
    base_url = models.URLField(default='https://www.weiyuai.cn')
    placement = models.CharField(
        max_length=20,
        choices=[
            ('bottom-right', 'Bottom Right'),
            ('bottom-left', 'Bottom Left'),
            ('top-right', 'Top Right'),
            ('top-left', 'Top Left'),
        ],
        default='bottom-right'
    )
    auto_popup = models.BooleanField(default=False)
    invite_show = models.BooleanField(default=False)
    invite_text = models.CharField(max_length=100, blank=True)
    bubble_show = models.BooleanField(default=True)
    bubble_icon = models.CharField(max_length=10, default='👋')
    bubble_title = models.CharField(max_length=100, default='需要帮助么')
    bubble_subtitle = models.CharField(max_length=100, default='点击我，与我对话')
    theme = models.CharField(
        max_length=20,
        choices=[
            ('system', 'System'),
            ('light', 'Light'),
            ('dark', 'Dark'),
        ],
        default='system'
    )
    background_color = models.CharField(max_length=20, default='#0066FF')
    text_color = models.CharField(max_length=20, default='#ffffff')
    window_width = models.CharField(max_length=10, default='380')
    org_id = models.CharField(max_length=100)
    type_id = models.CharField(max_length=10, default='2')
    sid = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ByteDesk Configuration'
        verbose_name_plural = 'ByteDesk Configurations' 