from django import template

register = template.Library()


@register.filter
def default_icon(icon_url):
    return icon_url if icon_url else '/static/images/default-icon.png'
