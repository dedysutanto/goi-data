from django.shortcuts import render
from parokia.models import Parokia, Komox
from django.conf import settings


def index(request):
    parokia = Parokia.objects.all()
    komox = Komox.objects.all()

    return render(request, 'index.html', {
        'parokia': parokia,
        'komox': komox,
        'settings': settings
    })
