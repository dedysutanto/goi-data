from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ButtonHelper, PermissionHelper)
from django.utils.translation import gettext_lazy as _
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel, ObjectList
from wagtailgeowidget import geocoders
from wagtailgeowidget.panels import GeoAddressPanel, GoogleMapsPanel
from .models import Member
from imagekit.admin import AdminThumbnail


#class MemberSVS(SnippetViewSet):
class MemberSVS(ModelAdmin):
    model = Member
    add_to_admin_menu = True
    menu_order = 200
    menu_label = _('Anggota')
    menu_icon = 'user'
    inspect_view_enabled = True
    photo_display = AdminThumbnail(image_field='photo_thumbnail')
    photo_display.short_description = 'Photo Thumbnail'
    list_display = ['__str__', 'photo_display']
    #list_display = ['__str__', 'dob']
    list_export = ['__str__', 'dob']
    search_fields = ['name', 'baptis_name', 'jabatan_klerus']
    #photo_display = AdminThumbnail(image_field='photo_thumbnail')
    panels = [
            MultiFieldPanel([
                FieldPanel('name'),
                FieldRowPanel([
                    FieldPanel('pob'),
                    FieldPanel('dob'),
                    FieldPanel('gender'),
                    ]),
                FieldRowPanel([
                    FieldPanel('email'),
                    FieldPanel('phone'),
                    ]),
                ], heading=_('Nama, Kelahiran dan Kontak')),
            MultiFieldPanel([
                GeoAddressPanel('address', geocoder=geocoders.GOOGLE_MAPS),
                GoogleMapsPanel('geolocation', address_field='address'),
                ], heading=_('Alamat')),
            MultiFieldPanel([
                FieldPanel('father'),
                FieldPanel('mother')
                ], heading=_('Data Orang Tua'), classname='collapsed'),
            MultiFieldPanel([
                FieldPanel('is_baptis', read_only=True),
                FieldRowPanel([
                    FieldPanel('baptis_name', read_only=True),
                    FieldPanel('baptis_number', read_only=True),
                    ]),
                FieldRowPanel([
                    FieldPanel('baptis_parent', read_only=True),
                    FieldPanel('baptis_klerus', read_only=True),
                    ]),
                FieldRowPanel([
                    FieldPanel('baptis_date', read_only=True),
                    FieldPanel('baptis_anniversary', read_only=True)
                    ]),
                ], heading=_('Data Baptis'), classname='collapsed'),
            MultiFieldPanel([
                FieldRowPanel([
                    FieldPanel('is_klerus', read_only=True),
                    FieldPanel('jabatan_klerus', read_only=True)
                    ])
                ], heading=_('Data Jabatan Klerus'), classname='collapsed'),
            MultiFieldPanel([
                FieldPanel('is_alive'),
                FieldPanel('photo')
                ], heading=_('Informasi Tambahan'), classname='collapsed')
            ]

#register_snippet(MemberSVS)
modeladmin_register(MemberSVS)

