from django.shortcuts import render
from django.http import JsonResponse
from box.models import Box, Income,TakenMoney
from django.utils import timezone


app_name = 'common'

def home_view(request):
    boxes = Box.objects.prefetch_related('takemoney', 'income').all()
    incomes = Income.objects.filter(created_at__month = timezone.now().month)
    takemoneys = TakenMoney.objects.filter(created_at__month = timezone.now().month)
    
    sum_income = 0
    sum_takemoney = 0
    for income in incomes:
        sum_income += income.amount
    
    for takemoney in takemoneys:
        sum_takemoney += takemoney.amount

    context = {
        'boxes': boxes,
        'incomes': sum_income,
        'takemoney': sum_takemoney,
        'box_count': boxes.count()
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