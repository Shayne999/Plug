from django import template
from chat.models import Notification

register = template.Library()

@register.inclusion_tag('show_notifications.html', takes_context=True)
def show_notifications(context):
    request_user = context['request'].user
    notifications = Notification.objects.filter(to_user=request_user, user_has_seen=False).order_by('-date')
    return {'notifications': notifications}
