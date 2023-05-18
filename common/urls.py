from django.urls import path, include
from . import views

app_name = 'common'
urlpatterns = [
    path('', views.cost, name='home')
]