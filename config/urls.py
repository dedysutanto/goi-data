from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from landing.views import index

admin.site.site_header = 'Gereja Orthodox Indonesia'

urlpatterns = [
    path('', index, name='index'),
    #path('', RedirectView.as_view(url='/admin')),
    path('admin/', admin.site.urls),
]

if not settings.PRODUCTION:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
