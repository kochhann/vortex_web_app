from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', include('apps.core.urls')),
    path('mngr/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'Gestão VG Switch'
admin.site.site_title = 'Gestão VG Switch'
admin.site.index_title = 'Área Administrativa'
