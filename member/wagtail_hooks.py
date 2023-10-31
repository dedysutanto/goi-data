from django.utils.translation import gettext_lazy as _
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel, ObjectList
from wagtailgeowidget import geocoders
from wagtailgeowidget.panels import GeoAddressPanel, GoogleMapsPanel
from .models import Member


class MemberSVS(SnippetViewSet):
    model = Member
    add_to_admin_menu = True
    menu_order = 200
    menu_label = _('Anggota')
    icon = 'doc-full'
    list_display = ['__str__', 'dob']
    list_export = ['__str__', 'dob']
    search_fields = ['name', 'baptis_name']
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
                FieldRowPanel([
                    FieldPanel('baptis_name', read_only=True),
                    FieldPanel('baptis_number', read_only=True),
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

register_snippet(MemberSVS)

