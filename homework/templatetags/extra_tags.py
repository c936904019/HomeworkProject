from django import template
register = template.Library()


@register.filter
def title(arr, i):
    return arr[int(i)].task_title


@register.filter
def value(arr, i):
    return arr[int(i)].value


@register.filter
def name(arr, i):
    return arr[int(i)].name


@register.filter
def count(arr):
    return range(len(arr))


@register.filter
def join(i, j):
    str_ij = str(i)+','+str(j)
    return str_ij


@register.filter
def index(str_ij, grades):
    i = str_ij.split(',')[0]
    j = str_ij.split(',')[1]
    return grades[int(i)][int(j)]
