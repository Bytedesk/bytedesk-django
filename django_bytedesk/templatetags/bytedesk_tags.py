from django import template
from django.utils.safestring import mark_safe
from ..models import BytedeskConfig

register = template.Library()

@register.simple_tag
def bytedesk_widget(config_name=None):
    try:
        if config_name:
            config = BytedeskConfig.objects.get(name=config_name, is_active=True)
        else:
            config = BytedeskConfig.objects.filter(is_active=True).first()
        
        if not config:
            return ''

        widget_config = {
            'baseUrl': config.base_url,
            'placement': config.placement,
            'autoPopup': config.auto_popup,
            'inviteParams': {
                'show': config.invite_show,
                'text': config.invite_text,
            },
            'bubbleConfig': {
                'show': config.bubble_show,
                'icon': config.bubble_icon,
                'title': config.bubble_title,
                'subtitle': config.bubble_subtitle
            },
            'theme': {
                'theme': config.theme,
                'backgroundColor': config.background_color,
                'textColor': config.text_color
            },
            'window': {
                'width': config.window_width
            },
            'chatParams': {
                'org': config.org_id,
                't': config.type_id,
                'sid': config.sid
            }
        }

        html = f'''
        <script src="https://www.weiyuai.cn/embed/bytedesk-web.js"></script>
        <script>
            const config = {widget_config};
            const bytedesk = new BytedeskWeb(config);
            bytedesk.init();
        </script>
        '''
        return mark_safe(html)
    except BytedeskConfig.DoesNotExist:
        return '' 