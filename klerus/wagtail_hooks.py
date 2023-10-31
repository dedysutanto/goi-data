from django.utils.translation import gettext_lazy as _
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register, ButtonHelper, PermissionHelper)
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel, ObjectList
from .models import JabatanKlerus, Klerus


#class JabatanKlerusSVS(SnippetViewSet):
class JabatanKlerusSVS(ModelAdmin):
    model = JabatanKlerus
    #add_to_admin_menu = True
    menu_icon = 'pick'
    list_display = ['name']


#class KlerusSVS(SnippetViewSet):
class KlerusSVS(ModelAdmin):
    model = Klerus
    #add_to_admin_menu = True
    menu_icon = 'user'
    menu_label = _('Klerus')
    list_display = ['name']

    panels = [
            MultiFieldPanel([
                FieldPanel('jabatan'),
                FieldPanel('name'),
                ])
            ]


#class KlerusSVSG(SnippetViewSetGroup):
class KlerusSVSG(ModelAdminGroup):
    add_to_admin_menu = True
    menu_icon = 'group'
    menu_label = _('Klerus')
    menu_order = 400
    items = [JabatanKlerusSVS, KlerusSVS]

#register_snippet(KlerusSVSG)
modeladmin_register(KlerusSVSG)

