from django import forms
from wagtail.users.forms import UserEditForm, UserCreationForm
from .models import User
from parokia.models import Parokia, Komox
from django.utils.translation import gettext_lazy as _


class CustomUserEditForm(UserEditForm):
    parokia = forms.ModelChoiceField(queryset=Parokia.objects,
                                          required=False,
                                          disabled=True,
                                          label=_("Parokia"))
    komox = forms.ModelChoiceField(queryset=Komox.objects,
                                          required=False,
                                          disabled=True,
                                          label=_("Komox"))


class CustomUserCreationForm(UserCreationForm):
    parokia = forms.ModelChoiceField(queryset=Parokia.objects,
                                          required=False,
                                          label=_("Parokia"))
    komox = forms.ModelChoiceField(queryset=Komox.objects,
                                          required=False,
                                          label=_("Komox"))
