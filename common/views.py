from django.shortcuts import render
from django.http import JsonResponse

app_name = 'common'

def home_view(request):
    return render(request, 'index.html')

