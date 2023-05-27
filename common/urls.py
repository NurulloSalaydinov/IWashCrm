from django.urls import path, include
from common.views import home_view, chart_box, withdrop
from django.conf import settings
from django.conf.urls.static import static
from box.views import update_info



app_name = 'common'
urlpatterns = [
    path('', home_view, name='home'),
    path('box/<slug:token>/chart', chart_box, name='chart'),
    path('box/<slug:token>/withdrop', withdrop, name='withdrop'),
     path('info-update/', update_info, name='update-info'),
]


# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)