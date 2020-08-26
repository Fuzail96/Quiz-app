from django import template

register = template.Library()


def get_index(lst, i):
    a=lst[i]
    return a.ans


register.filter("get_index", get_index)