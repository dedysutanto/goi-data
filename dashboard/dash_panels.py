from wagtail.admin.ui.components import Component
from django.conf import settings
#from crum import get_current_user
from django.utils.translation import gettext as _
from django.core.exceptions import ObjectDoesNotExist
#from monitor.models import MemberProblems
from member.wagtail_hooks import MemberSVS
from baptis.wagtail_hooks import BaptisSVS


class ShortcutsPanel(Component):
    order = 10
    template_name = "dashboard/shortcut_dashboard.html"

    def __init__(self):
        self.member_modeladmin = MemberSVS()
        self.baptis_modeladmin = BaptisSVS()

    def get_context_data(self, parent_context):
        context = super().get_context_data(parent_context)
        context['member_url_index'] = self.member_modeladmin.url_helper.index_url
        context['member_url_create'] = self.member_modeladmin.url_helper.create_url
        context['baptis_url_index'] = self.baptis_modeladmin.url_helper.index_url
        context['baptis_url_create'] = self.baptis_modeladmin.url_helper.create_url

        return context

