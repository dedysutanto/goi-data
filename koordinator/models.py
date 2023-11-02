from django.db import models
from django.utils.translation import gettext_lazy as _
from parokia.models import Parokia, Komox
from klerus.models import Klerus
from member.models import Member
from crum import get_current_user


class ParokiaKlerus(models.Model):
    def limit_choice_to_parokia():
        current_user = get_current_user()

        if current_user.is_superuser or current_user.username == 'admin':
            return {}
        else:
            if current_user.parokia:
                return {'id': current_user.parokia.id}
            else:
                return {'id': 0}

    parokia = models.ForeignKey(
            Parokia,
            on_delete=models.RESTRICT,
            verbose_name=_('Parokia'),
            limit_choices_to=limit_choice_to_parokia
            )

    klerus = models.ForeignKey(
            Klerus,
            on_delete=models.RESTRICT,
            verbose_name=_('Klerus')
            )

    class Meta:
        db_table = 'parokia_klerus'
        verbose_name = 'Parokia Klerus'
        verbose_name_plural = 'Parokia Klerus'

    def __str__(self):
        return '{} - {}'.format(self.parokia, self.klerus)


class KomoxKoordinator(models.Model):
    def limit_choice_to_komox():
        current_user = get_current_user()

        if current_user.is_superuser or current_user.username == 'admin':
            return {}
        else:
            if current_user.komox:
                return {'id': current_user.komox.id}
            elif current_user.parokia:
                return {'parokia': current_user.parokia}
            else:
                return {'id': 0}

    komox = models.ForeignKey(
            Komox,
            on_delete=models.RESTRICT,
            verbose_name=_('Komunitas Orthodox'),
            limit_choices_to=limit_choice_to_komox
            )
    koordinator = models.ForeignKey(
            Member,
            on_delete=models.RESTRICT,
            verbose_name=_('Koordinator')
            )

    class Meta:
        db_table = 'komox_koordinator'
        verbose_name = 'Komox Koordinator'
        verbose_name_plural = 'Komox Koordinator'

    def __str__(self):
        return '{} - {}'.format(self.komox, self.koordinator)

