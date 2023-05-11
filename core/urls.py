from django.contrib import admin
from django.urls import path
from common.views import cost

urlpatterns = [
    path('', cost, name='cost'),
    path('admin/', admin.site.urls),
]
