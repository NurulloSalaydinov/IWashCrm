from django.shortcuts import render
from django.http import JsonResponse



def cost(request):
    return JsonResponse({'voda': 47, 'vosk': 50, 'pena': 60, 'actpena': 100})

