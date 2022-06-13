from django.shortcuts import render
from parokia.models import Parokia, Komox
from django.conf import settings


def index(request):
    parokia = Parokia.objects.all()
    komox = Komox.objects.all()

    print(settings.GOOGLE_MAPS_API_KEY)
    print(settings.MAPS_CENTER)
    print(settings.MAPS_ZOOM)

    return render(request, 'index.html', {
        'parokia': parokia,
        'komox': komox,
        'settings': settings
    })
