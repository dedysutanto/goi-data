from django.contrib import admin
from .models import Parokia, Komox
#from django_google_maps import widgets as map_widgets
#from django_google_maps import fields as map_fields
from django import forms


class ParokiaAdmin(admin.ModelAdmin):
    ordering = ['name', 'code']
    search_fields = ('name', 'code')
    list_display = ['name', 'code', 'address']

    '''
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
    '''

    class Meta:
        model = Parokia


class KomoxAdmin(admin.ModelAdmin):
    ordering = ['name', 'code']
    search_fields = ('name', 'code')
    list_display = ['name', 'code', 'address']

    '''
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
    '''

    class Meta:
        model = Komox


admin.site.register(Parokia, ParokiaAdmin)
admin.site.register(Komox, KomoxAdmin)
