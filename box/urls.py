from django.urls import path
from .import views


app_name = 'box'


urlpatterns = [
    path('receive-money/', views.receive_money, name='receive-money'),
]


