from django.shortcuts import render, redirect

from django.http import JsonResponse

from django.utils import timezone

from django.contrib import messages

from .models import Box, Customer, Info, Income

from .forms import InfoForm


def get_info():
    info = Info.objects.first()
    return info


def get_today_income() -> Income:
    try:
        income = Income.objects.get(created_at__date=timezone.now().date(), box=None)
    except Income.DoesNotExist as e:
        print(f"Box does not exist {e}")
        income = Income.objects.create(box=None)
    except Income.MultipleObjectsReturned as e:
        print(f"Box does not exist {e}")
        income_list = list(Income.objects.filter(created_at__date=timezone.now().date(), box=None).order_by('-id'))
        for i in range(0,income_list.count()):
            income_list[i].delete()
    return income



def receive_money(request):
    token = request.GET.get('token', None)
    customer_id = request.GET.get('customer_id', None)
    summ = int(request.GET.get('amount', 0))
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
            customer.cash_back += int((cashback_percent * summ) / 100)
            # today income add
            today_income = get_today_income()
            today_income.amount += summ
            today_income.save()
            # today income box add
            box.cash += summ
            box.save()
            customer.save()
            return JsonResponse(response)
        # else
        # today income add
        today_income = get_today_income()
        today_income.amount += summ
        today_income.save()
        # today income box add
        box.cash += summ
        box.save()
        # return response
        return JsonResponse(response)
    except Box.DoesNotExist as e:
        # if box does not exist return error
        print(f"Box does not exist {e}")
        return JsonResponse({"error": "Invalid token"}, status=500)


def update_info(request):
    info = get_info()
    if request.method == "POST":
        form = InfoForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
            messages.success(request, "Narxlar o'zgartirildi")
            return redirect('/')
    context = {
        'info': info,
    }
    return render(request, 'update_info.html', context)
