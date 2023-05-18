from django.urls import path, include
from common.views import home_view

app_name = 'common'
urlpatterns = [
    path('', home_view, name='home')
]