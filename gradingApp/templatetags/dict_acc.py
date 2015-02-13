from django import template
register = template.Library()

@register.filter(name='access')
def access(value, arg,arg1):
    return value[arg][arg1]