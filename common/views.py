from django.shortcuts import render, redirect
from django.http import JsonResponse
from box.models import Box, Income,TakenMoney, Customer
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required 


app_name = 'common'


def home_view(request):
    boxes = Box.objects.prefetch_related('takemoney', 'income').all()
    incomes = Income.objects.filter(created_at__month = timezone.now().month)
    total_income = Income.objects.filter(box=None).order_by('created_at')
    takemoneys = TakenMoney.objects.filter(created_at__month = timezone.now().month)
    month = ['','Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr','Noyabr' 'Dekabr']
    value = []
    date = []
    for i in total_income:
        date.append(f"{month[i.created_at.month]} {i.created_at.day}")
        value.append(i.amount)

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
        'box_count': boxes.count(),
        'customer_count': Customer.objects.count(),
        'date': date,
        'value': value,
    }


    return render(request, 'main_com/index.html', context)

def chart_box(request, token):
    box = Box.objects.get(token = token)
    income = Income.objects.filter(box=box).order_by('created_at')
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
    return render(request, 'main_com/charts.html', context)

def withdrop(request, token):
    box = Box.objects.get(token = token)

    if request.method == 'POST':
        if box.cash != 0:
            TakenMoney.objects.create(box=box, amount=box.cash)
            box.cash = 0
            box.save()
            return redirect('common:home')
        else:
            messages.success(request, 'Qutiga pul yo\'q')
            return redirect(request.path)

    context = {
        'box': box
    }
    return render(request, 'main_com/get-money.html', context)