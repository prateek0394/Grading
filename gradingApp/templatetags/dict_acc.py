from django import template
register = template.Library()

@register.filter(name='access')
def access(value, arg):
	x = arg.split(';')
	return value[x[0]][x[1]]