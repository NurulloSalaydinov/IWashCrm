from django.http import JsonResponse
from django.shortcuts import render

from django.utils import timezone

from .models import Box, Customer, Info, Income


def get_info():
    info = Info.objects.first()
    return info


def get_today_income() -> Income:
    try:
        income = Income.objects.get(created_at__date=timezone.now().date())
    except Income.DoesNotExist as e:
        print("Couldn't find %" % e)
        income = Income.objects.create(created_at__date=timezone.now().date)
    except Income.MultipleObjectsReturned as e:
        print("Multiple objects returned %" % e)
        income_list = list(Income.objects.filter(created_at__date=timezone.now().date).order_by('-id'))
        for i in range(0,income_list.count()):
            income_list[i].delete()
    return income


def get_today_income_box(token: str) -> Income:
    try:
        income = Income.objects.get(created_at__date=timezone.now().date, box__token=token)
    except Income.DoesNotExist as e:
        print("Couldn't find %" % e)
        income = Income.objects.create(created_at__date=timezone.now().date, box__token=token)
    except Income.MultipleObjectsReturned as e:
        print("Multiple object returned %" % e)
        income_list = list(Income.objects.filter(created_at__date=timezone.now().date, box__token=token).order_by('-id'))
        for i in range(0,income_list.count()):
            income_list[i].delete()
    return income


def receive_money(request):
    token = request.GET.get('token', None)
    customer_id = request.GET.get('customer_id', None)
    amount = int(request.GET.get('amount', 0))
    info = get_info()
    water, wax, pena, active_pena, cashback_use = info.water, info.wax, info.pena, info.active_pena, info.cashback_use

    cashback_percent = info.cashback_percent

    # preparing response
    response = {
        "voda": water,
        "vosk": wax,
        "pena": pena,
        "actpena": active_pena,
        "usage": cashback_use
    }

    try:
        # trying to get box
        box = Box.objects.get(token=token)
        if customer_id:
            try:
                customer = Customer.objects.get(turniket_id=customer_id)
            except Customer.DoesNotExist as e:
                customer = Customer.objects.create(turniket_id=customer_id)
            customer.cash_back += int(cashback_percent * amount / 100)
            # today income add
            today_income = get_today_income()
            today_income.amount += int(amount)
            today_income.save()
            # today income box add
            today_income_box = get_today_income_box(box.token)
            today_income_box.amount += int(amount)
            today_income_box.save()
            customer.save()
            return JsonResponse(response)
        # else
        today_income = get_today_income()
        today_income.amount += int(amount)
        today_income.save()
        # today income box add
        today_income_box = get_today_income_box(box.token)
        today_income_box.amount += int(amount)
        today_income_box.save()
        # return response
        return JsonResponse(response)
    except Box.DoesNotExist as e:
        # if box does not exist return error
        print("Box does not exist %" % e)
        return JsonResponse({"error": "Invalid token"}, status=0)

 