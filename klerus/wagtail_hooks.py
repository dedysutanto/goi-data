from django.utils.translation import gettext_lazy as _
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel, ObjectList
from .models import JabatanKlerus, Klerus


class JabatanKlerusSVS(SnippetViewSet):
    model = JabatanKlerus
    #add_to_admin_menu = True
    icon = 'pick'
    list_display = ['name']

class KlerusSVS(SnippetViewSet):
    model = Klerus
    #add_to_admin_menu = True
    icon = 'user'
    menu_label = _('Klerus')
    list_display = ['name']

    panels = [
            MultiFieldPanel([
                FieldPanel('jabatan'),
                FieldPanel('name'),
                ])
            ]

class KlerusSVSG(SnippetViewSetGroup):
    add_to_admin_menu = True
    menu_icon = 'group'
    menu_label = _('Klerus')
    menu_order = 400
    items = [JabatanKlerusSVS, KlerusSVS]

register_snippet(KlerusSVSG)

