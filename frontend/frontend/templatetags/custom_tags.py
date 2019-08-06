from operator import itemgetter

from django import template
register = template.Library()

@register.filter
def sort_by(lst, value):
    return sorted(lst, key=itemgetter(value))