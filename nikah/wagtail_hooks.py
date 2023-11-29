from django.utils.translation import gettext_lazy as _
from wagtail.admin.viewsets import model
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ButtonHelper, PermissionHelper)
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel, ObjectList
from .models import Nikah


#class BaptisSVS(SnippetViewSet):
class NikahSVS(ModelAdmin):
    model = Nikah
    add_to_admin_menu = True
    icon = 'calendar-check'
    menu_icon = 'calendar-check'
    menu_order = 300
    menu_label = _('Sakramen Pernikahan')
    list_display = ['suami', 'istri', 'nikah_klerus', 'pendamping_suami', 'pendamping_istri', 'number', 'parokia']
    search_fields = ['suami__name', 'istri__name', 'parokia__name']
    panels = [
            MultiFieldPanel([
                FieldPanel('suami'),
                FieldPanel('istri'),
                FieldPanel('nikah_klerus'),
                FieldPanel('pendamping_suami'),
                FieldPanel('pendamping_istri'),
                FieldPanel('parokia'),
                FieldRowPanel([
                    FieldPanel('nikah_date'),
                    FieldPanel('number'),
                ]),
                ], heading=_('Data Pernikahan')),
            ]

    def get_queryset(self, request):
        if request.user.is_superuser or request.user.username == 'admin':
            return Nikah.objects.all()
        else:
            if request.user.komox:
                return Nikah.objects.filter(komox=request.user.komox)
            elif request.user.parokia:
                return Nikah.objects.filter(parokia=request.user.parokia)
            else:
                return Nikah.objects.none()


#register_snippet(BaptisSVS)
modeladmin_register(NikahSVS)

