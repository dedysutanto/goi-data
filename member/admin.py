from django.contrib import admin
from .models import Member
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from django import forms
from imagekit.admin import AdminThumbnail


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
            'classes': ('',),
            'fields': ('name', ('pob', 'dob'), 'photo', 'photo_display')
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
            'fields': ('baptis_number', 'baptis_name', 'baptis_anniversary', 'baptis_date',),
        }),
    )
    list_display = ['name', 'pob', 'dob', 'address', 'phone', 'email', 'photo_display']
    photo_display = AdminThumbnail(image_field='photo_thumbnail')
    photo_display.short_description = 'Photo Thumbnail'
    readonly_fields = ['photo_display']
    search_fields = ('name', 'dob')

    class Meta:
        model = Member


admin.site.register(Member, MemberAdmin)
