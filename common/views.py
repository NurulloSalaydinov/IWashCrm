from django.shortcuts import render
from django.http import JsonResponse
from box.models import Box, Income,TakenMoney

app_name = 'common'

def home_view(request):
    boxes = Box.objects.prefetch_related('takemoney', 'income').all()
    context = {
        'boxes': boxes
    }

    return render(request, 'index.html', context)

def chart_box(request, token):
    box = Box.objects.get(token = token)
    income = Income.objects.filter(box=box)
    month = ['','Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr','Noyabr' 'Dekabr']
    value = []
    date = []
    for i in income:
        date.append(f"{month[i.created_at.month]} {i.created_at.day}")
        value.append(i.amount)

    print(date)
    print(value)
    context = {
        'box': box,
        'date' : date,
        'value': value
    }
    return render(request, 'charts.html', context)