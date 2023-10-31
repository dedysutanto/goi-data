from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from landing.views import index
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

admin.site.site_header = 'Gereja Orthodox Indonesia'

urlpatterns = [
    #path('', index, name='index'),
    path('', include('landing.urls')),
    path('admin/', include(wagtailadmin_urls)),
    #path('', RedirectView.as_view(url='/admin')),
    path('django-admin/', admin.site.urls),
]

#if not settings.PRODUCTION:
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
