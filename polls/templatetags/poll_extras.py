from django import template
from jalali_date import date2jalali

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, "")


@register.filter(name='show_date2jalali')
def show_jalali_date(value):
    return date2jalali(value)


@register.filter(name='show_time')
def show_time(value):
    return value.strftime('%H:%M')