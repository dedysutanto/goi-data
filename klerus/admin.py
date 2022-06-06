from django.contrib import admin
from .models import Klerus


class KlerusAdmin(admin.ModelAdmin):
    #search_fields = ('name',)
    list_display = ['__str__']

    class Meta:
        model = Klerus


admin.site.register(Klerus, KlerusAdmin)