from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('common.urls', namespace='common')),
    path('api/v1/', include('box.urls', namespace='box')),
    path('admin/', admin.site.urls),
]
