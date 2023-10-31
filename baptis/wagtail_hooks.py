from django.utils.translation import gettext_lazy as _
from wagtail.admin.viewsets import model
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ButtonHelper, PermissionHelper)
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel, ObjectList
from .models import Baptis


#class BaptisSVS(SnippetViewSet):
class BaptisSVS(ModelAdmin):
    model = Baptis
    add_to_admin_menu = True
    icon = 'snippet'
    menu_icon = 'snippet'
    menu_order = 300
    menu_label = _('Baptis')
    list_display = ['member', 'baptis_parent', 'baptis_klerus', 'baptis_date', 'parokia']
    panels = [
            MultiFieldPanel([
                FieldRowPanel([
                    FieldPanel('member'),
                    FieldPanel('parokia'),
                ]),
                FieldRowPanel([
                    FieldPanel('baptis_parent'),
                    FieldPanel('baptis_klerus'),
                ]),
                FieldPanel('baptis_name'),
                FieldRowPanel([
                    FieldPanel('baptis_date'),
                    FieldPanel('baptis_anniversary'),
                ]),
                FieldPanel('number'),
                ], heading=_('Data Baptis')),
            ]

#register_snippet(BaptisSVS)
modeladmin_register(BaptisSVS)

