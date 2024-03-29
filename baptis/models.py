from django.db import models
from parokia.models import Parokia, Komox
from member.models import Member
from klerus.models import Klerus
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import gettext_lazy as _
from crum import get_current_user


class Baptis(models.Model):
    def limit_choices_baptis():
        return {'is_baptis': True}

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

    def limit_choices_komox():
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


    parokia = models.ForeignKey(
        Parokia,
        on_delete=models.RESTRICT,
        verbose_name=_('Parokia'),
        null=True,
        blank=True,
        limit_choices_to=limit_choices_parokia
    )

    komox = models.ForeignKey(
        Komox,
        on_delete=models.RESTRICT,
        verbose_name=_('Komox'),
        null=True,
        blank=True,
        limit_choices_to=limit_choices_komox
            )
    #number = models.CharField(max_length=30, unique=True, verbose_name='Nomor Sertifikat Baptis')
    number = models.CharField(max_length=30, blank=True, null=True, verbose_name='Nomor Sertifikat Baptis')
    member = models.OneToOneField(
        Member,
        on_delete=models.RESTRICT,
        related_name='baptis_member_related',
        verbose_name='Yang Di Baptis',
        #limit_choices_to=limit_choices_non_baptis,
        #null=True,
        #blank=True
    )
    baptis_parent = models.ForeignKey(
        Member,
        on_delete=models.RESTRICT,
        related_name='baptis_parent_related',
        verbose_name='Orang Tua Baptis',
        limit_choices_to=limit_choices_baptis,
        null=True,
        blank=True
    )
    baptis_klerus = models.ForeignKey(
        Klerus,
        on_delete=models.RESTRICT,
        verbose_name='Klerus Yang Membaptis',
        null=True,
        blank=True
    )
    baptis_name = models.CharField(max_length=50, verbose_name='Nama Baptis')
    baptis_anniversary = models.DateField(null=True, blank=True, verbose_name='Tanggal Peringatan')
    baptis_date = models.DateField(null=True, blank=True, verbose_name='Tanggal Baptis')

    #is_baptis_name_from_name = models.BooleanField(_('Nama baptis diambil dari nama asli'), default=False)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'baptis'
        verbose_name = 'Baptis'
        verbose_name_plural = 'Daftar Baptis'
        
    def __str__(self):
        return '%s' % self.number

    def clean(self):
        if self.member == self.baptis_parent:
            raise ValidationError({'baptis_parent': _('Orang tua baptis tidak boleh sama dengan yang di baptis')})

    def save(self, *args, **kwargs):
        if self.number is not None:
            self.number = self.number.upper()

        self.baptis_name = self.baptis_name.upper()
        '''
        try:
            member = Member.objects.get(id=self.member.id)
            member.baptis_number = self.number
            member.baptis_name = self.baptis_name
            member.baptis_anniversary = self.baptis_anniversary
            member.baptis_date = self.baptis_date
            member.save()
        except ObjectDoesNotExist:
            raise ValidationError({'member': [_('Yang Dibaptis Tidak Boleh Kosong!')]})
        '''
        return super(Baptis, self).save(*args, **kwargs)
