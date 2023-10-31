from django.utils.translation import gettext_lazy as _
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel, ObjectList
from wagtailgeowidget import geocoders
from wagtailgeowidget.panels import GeoAddressPanel, GoogleMapsPanel
from .models import Parokia, Komox


class ParokiaSVS(SnippetViewSet):
    model = Parokia
    add_to_admin_menu = True
    icon = 'home'
    menu_order = 100
    menu_label = _('Parokia')
    list_display = ['name', 'code', 'address', 'klerus_1', 'klerus_2']
    search_fields = ['name', 'code', 'address']
    panels = [
            MultiFieldPanel([
                FieldPanel('name'),
                FieldPanel('code'),
                ], heading=_('Nama dan Kode')),
            MultiFieldPanel([
                GeoAddressPanel('address', geocoder=geocoders.GOOGLE_MAPS),
                GoogleMapsPanel('geolocation', address_field='address'),
                ], heading=_('Alamat')),
            MultiFieldPanel([
                FieldRowPanel([
                    FieldPanel('klerus_1'),
                    FieldPanel('klerus_2')
                    ])
                ], heading=_('Klerus yang bertanggung jawab')),
            ]

register_snippet(ParokiaSVS)

