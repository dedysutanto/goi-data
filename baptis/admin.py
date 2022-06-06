from django.contrib import admin
from .models import Baptis


class BaptisAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'classes': ('',),
            'fields': ('parokia', 'baptis_date', 'number')
        }),
        (None, {
            'classes': ('',),
            'fields': ('member', 'baptis_klerus', 'baptis_parent')
        }),
        (None, {
            'classes': ('',),
            'fields': ('baptis_name', 'baptis_anniversary')
        }),
    )

    list_display = ['number', 'baptis_date', 'member', 'baptis_name',
                    'baptis_parent', 'baptis_klerus', 'baptis_anniversary']
    search_fields = ('number', 'member__name', 'member__baptis_name',
                     'baptis_parent__name', 'baptis_klerus__name__name', 'baptis_klerus__name__baptis_name')
    ordering = ['number']
    list_per_page = 25

    class Meta:
        model = Baptis


admin.site.register(Baptis, BaptisAdmin)