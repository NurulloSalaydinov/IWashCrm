from django.urls import path, include
from common.views import home_view, chart_box

app_name = 'common'
urlpatterns = [
    path('', home_view, name='home'),
    path('box/<slug:token>/chart', chart_box, name='chart')
]