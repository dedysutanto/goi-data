from django.utils.translation import gettext_lazy as _
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register, ButtonHelper, PermissionHelper)
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel, ObjectList
from .models import Etnik, Pendidikan, Pekerjaan, Nob


#class JabatanKlerusSVS(SnippetViewSet):
class PendidikanSVS(ModelAdmin):
    model = Pendidikan
    add_to_settings_menu = True
    exclude_from_explorer = False
    menu_icon = 'cog'
    menu_label = _('Pendidikan')
    list_display = ['name']


class PekerjaanSVS(ModelAdmin):
    model = Pekerjaan
    add_to_settings_menu = True
    exclude_from_explorer = False
    menu_icon = 'cog'
    menu_label = _('Pekerjaan')
    list_display = ['name']



class NobSVS(ModelAdmin):
    model = Nob
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ['name']
    menu_label = _('Nature of Business')
    menu_icon = 'cog'


class EtnikSVS(ModelAdmin):
    model = Etnik
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ['name']
    menu_label = _('Etnik')
    menu_icon = 'cog'

'''
class DataSupportSVSG(ModelAdminGroup):
    add_to_settings_menu = True
    exclude_from_explorer = False
    menu_label = _('Data Support')
    menu_icon = 'cogs'
    items = [PendidikanSVS, PekerjaanSVS, NobSVS]
'''



#register_snippet(KlerusSVSG)
#modeladmin_register(DataSupportSVSG)
modeladmin_register(PendidikanSVS)
modeladmin_register(PekerjaanSVS)
modeladmin_register(NobSVS)
modeladmin_register(EtnikSVS)

