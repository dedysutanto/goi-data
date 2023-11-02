from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from parokia.models import Parokia, Komox


class User(AbstractUser):
    parokia = models.ForeignKey(
        Parokia,
        on_delete=models.SET_NULL,
        verbose_name=_('Parokia'),
        blank=True,
        null=True,
    )

    komox = models.ForeignKey(
        Komox,
        on_delete=models.SET_NULL,
        verbose_name=_('Komox'),
        blank=True,
        null=True,
    )

