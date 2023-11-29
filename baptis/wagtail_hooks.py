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
    icon = 'calendar-check'
    menu_icon = 'calendar-check'
    menu_order = 300
    menu_label = _('Sakramen Baptis')
    list_display = ['member', 'baptis_parent', 'baptis_klerus', 'baptis_date', 'parokia', 'komox']
    search_fields = ['member__name', 'member__jabatan_klerus', 'member__baptis_name', 'parokia__name']
    panels = [
            MultiFieldPanel([
                FieldPanel('member'),
                FieldPanel('baptis_name'),
                FieldRowPanel([
                    FieldPanel('baptis_parent'),
                    FieldPanel('baptis_klerus'),
                ]),
                FieldRowPanel([
                    FieldPanel('parokia'),
                    FieldPanel('komox'),
                ]),
                FieldRowPanel([
                    FieldPanel('baptis_date'),
                    FieldPanel('baptis_anniversary'),
                ]),
                FieldPanel('number'),
                ], heading=_('Data Baptis')),
            ]

    def get_queryset(self, request):
        if request.user.is_superuser or request.user.username == 'admin':
            return Baptis.objects.all()
        else:
            if request.user.komox:
                return Baptis.objects.filter(komox=request.user.komox)
            elif request.user.parokia:
                return Baptis.objects.filter(parokia=request.user.parokia)
            else:
                return Baptis.objects.none()


#register_snippet(BaptisSVS)
modeladmin_register(BaptisSVS)

