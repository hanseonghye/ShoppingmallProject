from operator import itemgetter

from django import template
register = template.Library()

@register.filter
def sort_by(lst, value):
    return sorted(lst, key=itemgetter(value))

@register.filter
def unsort_by(lst, value):
    return sorted(lst, key=itemgetter(value), reverse=True)