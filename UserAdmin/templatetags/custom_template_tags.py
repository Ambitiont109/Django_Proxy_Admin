from django import template
from django.urls import reverse
from UserAdmin.models import User
register = template.Library()


@register.simple_tag
def navactive(request, urls):
    if request.path in (reverse(url) for url in urls.split()):
        return "active"
    return ""


@register.simple_tag
def getUserCount():
    return User.objects.exclude(is_superuser=True).count()


@register.filter(name='MBFormat')  # Custom Filter
def MBFormat(byte_value):
    mb_value = byte_value / 1024 / 1024
    return '%.2f MB' % mb_value
