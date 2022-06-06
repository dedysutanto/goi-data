from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

admin.site.site_header = 'Gereja Orthodox Indonesia'

urlpatterns = [
    path('', RedirectView.as_view(url='/admin')),
    path('admin/', admin.site.urls),
]
