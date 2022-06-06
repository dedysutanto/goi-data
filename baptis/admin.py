from django.contrib import admin
from .models import Baptis


class BaptisAdmin(admin.ModelAdmin):

    list_display = ['number', 'member', 'baptis_parent', 'baptis_klerus', 'baptis_name', 'baptis_date', 'baptis_anniversary']
    search_fields = ('number', 'member__name', 'baptis_parent__name', 'baptis_klerus__name')

    class Meta:
        model = Baptis


admin.site.register(Baptis, BaptisAdmin)