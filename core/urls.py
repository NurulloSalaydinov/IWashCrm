from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('common.urls', namespace='common')),
    path('admin/', admin.site.urls),
]
