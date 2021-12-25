from django import template


register = template.Library()


@register.filter
def range_value(value):
    """ Returns the range of value """
    return range(1, value + 1)
