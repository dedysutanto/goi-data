from django.utils.translation import gettext_lazy as _
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register, ButtonHelper, PermissionHelper)
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, FieldRowPanel, ObjectList
from wagtailgeowidget import geocoders
from wagtailgeowidget.panels import GeoAddressPanel, GoogleMapsPanel
from .models import Parokia, Komox, MemberParokia
from koordinator.models import ParokiaKlerus, KomoxKoordinator
from django.db.models import Q
from crum import get_current_user


class ParokiaPH(PermissionHelper):
    def user_can_list(self, user):
        return True

    def user_can_create(self, user):
        current_user = get_current_user()
        if current_user.is_superuser or current_user.username == 'admin':
            return True
        else:
            return False

    '''
    def user_can_delete_obj(self, user, obj):
        current_user = get_current_user()
        if current_user.is_superuser or current_user.username == 'admin':
            return True
        else:
            return False
        return False
    '''

    def user_can_edit_obj(self, user, obj):
        current_user = get_current_user()
        if current_user.is_superuser or current_user.username == 'admin':
            return True
        else:
            if current_user.komox:
                return False

            if current_user.parokia == obj:
                return True
            else:
                return False


class KomoxPH(PermissionHelper):
    def user_can_list(self, user):
        return True

    def user_can_create(self, user):
        current_user = get_current_user()
        if current_user.is_superuser or current_user.username == 'admin':
            return True
        else:
            return False

    '''
    def user_can_delete_obj(self, user, obj):
        current_user = get_current_user()
        if current_user.is_superuser or current_user.username == 'admin':
            return True
        else:
            return False
        return False
    '''

    def user_can_edit_obj(self, user, obj):
        current_user = get_current_user()
        if current_user.is_superuser or current_user.username == 'admin':
            return True
        else:
            if current_user.komox:
                if current_user.komox == obj:
                    return True
                else:
                    return False

            elif current_user.parokia == obj.parokia:
                return True
            else:
                return False

class MemberParokiaPH(PermissionHelper):
    def user_can_list(self, user):
        return True

    def user_can_create(self, user):
        current_user = get_current_user()
        if current_user.is_superuser or current_user.username == 'admin':
            return True
        else:
            return False

    '''
    def user_can_delete_obj(self, user, obj):
        current_user = get_current_user()
        if current_user.is_superuser or current_user.username == 'admin':
            return True
        else:
            return False
        return False
    '''

    def user_can_edit_obj(self, user, obj):
        current_user = get_current_user()
        if current_user.is_superuser or current_user.username == 'admin':
            return True
        else:
            if current_user.komox:
                if current_user.komox == obj.komox:
                    return True
                else:
                    return False
            elif current_user.parokia == obj.parokia:
                return True
            else:
                return False

#class ParokiaSVS(SnippetViewSet):
class ParokiaSVS(ModelAdmin):
    model = Parokia
    add_to_admin_menu = False
    permission_helper_class = ParokiaPH
    menu_icon = 'home'
    #menu_order = 100
    menu_label = _('Parokia')
    list_display = ['name', 'code', 'address', 'description' ]
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
                    FieldPanel('email'),
                    FieldPanel('phone'),
                    ]),
                FieldPanel('description'),
                ], heading=_('Email, Phone dan Catatan')),
            ]

class KomoxSVS(ModelAdmin):
    model = Komox
    add_to_admin_menu = False
    permission_helper_class = KomoxPH
    menu_icon = 'group'
    #menu_order = 100
    menu_label = _('Komox')
    list_display = ['name', 'code', 'address', 'parokia', 'klerus']
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
                FieldPanel('parokia'),
                FieldPanel('klerus'),
                ], heading=_('Parokia dan Klerus yang melayani')),
            ]

class ParokiaKlerusSVS(ModelAdmin):
    model = ParokiaKlerus
    add_to_admin_menu = False
    menu_icon = 'pick'
    #menu_order = 100
    menu_label = _('Parokia Klerus')
    list_display = ['parokia', 'klerus']
    search_fields = ['parokia', 'klerus']
    panels = [
            MultiFieldPanel([
                FieldPanel('parokia'),
                FieldPanel('klerus'),
                ], heading=_('Parokia dan Klerus')),
            ]


class KomoxKoordinatorSVS(ModelAdmin):
    model = KomoxKoordinator
    add_to_admin_menu = False
    menu_icon = 'user'
    #menu_order = 100
    menu_label = _('Komox Koordinator')
    list_display = ['komox', 'koordinator']
    search_fields = ['komox', 'koordinator']
    panels = [
            MultiFieldPanel([
                FieldPanel('komox'),
                FieldPanel('koordinator'),
                ], heading=_('Komox dan Koordinator')),
            ]


class MemberParokiaSVS(ModelAdmin):
    model = MemberParokia
    add_to_admin_menu = True
    permission_helper_class = MemberParokiaPH
    menu_icon = 'clipboard-list'
    menu_order = 250
    menu_label = _('Anggota Parokia dan Komox')
    list_display = ['member', 'parokia', 'komox']
    #list_filter = ['parokia', 'komox']
    search_fields = ['member', 'parokia', 'komox']
    panels = [
            MultiFieldPanel([
                FieldPanel('member'),
                FieldPanel('parokia'),
                FieldPanel('komox'),
                ], heading=_('Keanggotaan di Parokia dan Komox')),
            ]

    def get_queryset(self, request):
        if request.user.is_superuser or request.user.username == 'admin':
            return MemberParokia.objects.all()
        else:
            if request.user.komox:
                return MemberParokia.objects.filter(
                        Q(komox=request.user.komox) | 
                        Q(parokia=request.user.komox.parokia)
                        )
            elif request.user.parokia:
                return MemberParokia.objects.filter(Q(parokia=request.user.parokia))
            else:
                return MemberParokia.objects.none()



class ParokiaSVSG(ModelAdminGroup):
    menu_icon = 'home'
    menu_order = 100
    menu_label = _('Parokia dan Komox')
    items = [ParokiaSVS, ParokiaKlerusSVS, KomoxSVS, KomoxKoordinatorSVS]

#register_snippet(ParokiaSVS)
modeladmin_register(ParokiaSVSG)
modeladmin_register(MemberParokiaSVS)

