from django.contrib import admin
from django.urls import path, include
from common.views import cost

urlpatterns = [
    path('', include('common.urls', namespace='common')),
    path('admin/', admin.site.urls),
]
