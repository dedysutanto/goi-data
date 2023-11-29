from django.db import models
from parokia.models import Parokia, Komox
from member.models import Member
from klerus.models import Klerus
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import gettext_lazy as _
from crum import get_current_user


class Nikah(models.Model):
    def limit_choices_baptis():
        return {'is_baptis': True}

    def limit_choices_baptis_suami():
        return {'is_baptis': True, 'gender': 'L'}

    def limit_choices_baptis_istri():
        return {'is_baptis': True, 'gender': 'P'}

    def limit_choices_non_baptis():
        return {'is_baptis': False}

    def limit_choices_parokia():
        current_user = get_current_user()
        if current_user.is_superuser or current_user.username == 'admin':
            return {}
        else:
            if current_user.parokia:
                return {'id': current_user.parokia.id}
            else:
                return {'id': 0}

    
    suami = models.OneToOneField(
        Member,
        on_delete=models.RESTRICT,
        related_name='nikah_suami_related',
        verbose_name='Suami',
        limit_choices_to=limit_choices_baptis_suami,
        #null=True,
        #blank=True
    )

    istri = models.OneToOneField(
        Member,
        on_delete=models.RESTRICT,
        related_name='nikah_istri_related',
        verbose_name='Istri',
        limit_choices_to=limit_choices_baptis_istri,
        #null=True,
        #blank=True
    )

    pendamping_suami = models.ForeignKey(
        Member,
        on_delete=models.RESTRICT,
        related_name='pendamping_suami_related',
        verbose_name='Pendamping Suami',
        limit_choices_to=limit_choices_baptis_suami,
        null=True,
        blank=True
    )

    pendamping_istri = models.ForeignKey(
        Member,
        on_delete=models.RESTRICT,
        related_name='pendamping_istri_related',
        verbose_name='Pendamping Istri',
        limit_choices_to=limit_choices_baptis_istri,
        null=True,
        blank=True
    )

    nikah_klerus = models.ForeignKey(
        Klerus,
        on_delete=models.RESTRICT,
        verbose_name='Klerus Yang Menikahkan',
        null=True,
        blank=True
    )

    number = models.CharField(max_length=30, blank=True, null=True, verbose_name='Nomor Sertifikat Nikah')
    nikah_date = models.DateField(null=True, blank=True, verbose_name='Tanggal Nikah')

    parokia = models.ForeignKey(
        Parokia,
        on_delete=models.RESTRICT,
        verbose_name=_('Parokia'),
        null=True,
        blank=True,
        limit_choices_to=limit_choices_parokia
    )

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


    class Meta:
        db_table = 'nikah'
        verbose_name = 'Pernikahan'
        verbose_name_plural = 'Pernikahan'

    def __str__(self):
        return '%s' % self.number

    def save(self, *args, **kwargs):
        if self.number is not None:
            self.number = self.number.upper()

        return super(Nikah, self).save(*args, **kwargs)

