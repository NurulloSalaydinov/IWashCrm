from django.http import JsonResponse
from django.shortcuts import render





def receive_money(request):
    token = request.GET.get('token', None)
    customer_id = request.GET.get('customer_id', None)

    return JsonResponse({"error": "Something went wrong!"})
