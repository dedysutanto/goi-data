from django.contrib import admin
from .models import Member
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from django import forms


class MemberAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={
              'data-map-type': 'roadmap',
              'placeholder': 'Masukkan alamat dan tekan enter',
              'size': 200
          })
        },
        map_fields.GeoLocationField: {
            'widget': forms.TextInput(attrs={
                'readonly': 'readonly',
                'size': 100
            })
        },
    }

    fieldsets = (
        (None, {
            'fields': ('name', ('pob', 'dob'),)
        }),
        ('Orang Tua', {
            'classes': ('collapse',),
            'fields': ('father', 'mother'),
        }),
        ('Kontak', {
            'classes': ('collapse',),
            'fields': ('email', 'phone', 'address', 'geolocation'),
        }),
        ('Baptis', {
            'classes': ('collapse',),
            'fields': ('baptis_name', 'baptis_anniversary', 'baptis_date',),
        }),
    )
    list_display = ['name', 'pob', 'dob', 'address', 'phone', 'email']
    search_fields = ('name', 'dob')

    class Meta:
        model = Member


admin.site.register(Member, MemberAdmin)
