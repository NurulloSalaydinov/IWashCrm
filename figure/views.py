from django.shortcuts import render
from box.models import Income, Customer, Box
from box.views import get_today_income




def get_customer_count():
    customer_count = Customer.objects.all().count()
    return customer_count



def home_view(request):
    boxes = Box.objects.all()
    context = {
        "income": get_today_income(),
        "boxes": boxes,
    }
    return render(request, 'index.html', context)





