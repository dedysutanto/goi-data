from django.db import models
#from django_google_maps import fields as map_fields
#from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from klerus.models import Klerus
from member.models import Member
from crum import get_current_user


class Parokia(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nama Parokia')
    code = models.CharField(max_length=20, 
                            unique=True, 
                            verbose_name=_('Kode Parokia'),
                            help_text=_('Kode Parokia bisa menggunakan singkatan. Contoh: JSPP untuk Js Petrus dan Paulus'))
    address = models.CharField(max_length=250, blank=True, verbose_name='Alamat')
    geolocation = models.CharField(max_length=250, blank=True, verbose_name='Koordinat GoogleMap')
    #address = map_fields.AddressField(max_length=200, blank=True, verbose_name='Alamat')
    #geolocation = map_fields.GeoLocationField(max_length=100, blank=True, verbose_name='Koordinat GoogleMap')
    email = models.EmailField(max_length=50, blank=True, verbose_name='Alamat Email')
    phone = models.CharField(max_length=20, verbose_name='Telpon/HP', blank=True)

    '''
    klerus_1 = models.ForeignKey(
        Klerus,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='Nama Klerus 1',
        related_name='parokia_klerus_1',
    )
    klerus_2 = models.ForeignKey(
        Klerus,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='Nama Klerus 2',
        related_name='parokia_klerus_2',
    )
    '''

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'parokia'
        verbose_name = 'Parokia'
        verbose_name_plural = 'Daftar Parokia'

    def __str__(self):
        return '%s' % self.name

    def clean(self, *args, **kwargs):
        self.name = self.name.upper()
        self.code = self.code.upper()


class Komox(models.Model):
    def limit_choices_to_parokia():
        current_user = get_current_user()
        if current_user.is_superuser or current_user.username == 'admin':
            return {}
        else:
            if current_user.parokia:
                return {'id': current_user.parokia.id}
            else:
                return {'id': 0}

    name = models.CharField(max_length=200, verbose_name='Nama Komox')
    code = models.CharField(max_length=20, unique=True, verbose_name='Kode Komox')
    address = models.CharField(max_length=250, blank=True, verbose_name='Alamat')
    geolocation = models.CharField(max_length=250, blank=True, verbose_name='Koordinat GoogleMap')
    #address = map_fields.AddressField(max_length=200, blank=True, verbose_name='Alamat')
    #geolocation = map_fields.GeoLocationField(max_length=100, blank=True, verbose_name='Koordinat GoogleMap')
    email = models.EmailField(max_length=50, blank=True, verbose_name='Alamat Email')
    phone = models.CharField(max_length=20, verbose_name='Telpon/HP', blank=True)
    klerus = models.ForeignKey(
            Klerus,
            on_delete=models.RESTRICT,
            verbose_name=_('Klerus'),
            blank=True,
            null=True
            )
    parokia = models.ForeignKey(
            Parokia,
            on_delete=models.RESTRICT,
            verbose_name=_('Parokia'),
            related_name='parokia_komox',
            limit_choices_to=limit_choices_to_parokia
            )

    '''
    koordinator_1 = models.ForeignKey(
        Member,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='Koordinator 1',
        related_name='koordinator_1',
    )
    koordinator_2 = models.ForeignKey(
        Member,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='Koordinator 2',
        related_name='koordinator_2',
    )
    '''

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'komox'
        verbose_name = 'Komunitas Orthodox'
        verbose_name_plural = 'Daftar Komox'

    def __str__(self):
        return '%s' % self.name

    def clean(self, *args, **kwargs):
        self.name = self.name.upper()
        self.code = self.code.upper()


class MemberParokia(models.Model):
    def limit_choices_to_parokia():
        current_user = get_current_user()
        if current_user.is_superuser or current_user.username == 'admin':
            return {}
        else:
            if current_user.parokia:
                return {'parokia': current_user.parokia}
            else:
                #return {'parokia': None}
                return {'id': 0}

    member = models.OneToOneField(
            Member,
            on_delete=models.CASCADE,
            verbose_name=_('Anggota')
            )
    parokia = models.ForeignKey(
            Parokia,
            on_delete=models.CASCADE,
            verbose_name=_('Parokia'),
            blank=True,
            null=True
            )
    komox = models.ForeignKey(
            Komox,
            on_delete=models.CASCADE,
            verbose_name=_('Komox'),
            blank=True,
            null=True,
            limit_choices_to=limit_choices_to_parokia
            )

    class Meta:
        db_table = 'member_parokia'
        verbose_name = _('Anggota Parokia dan Komox')
        verbose_name_plural = _('Anggota Parokia dan Komox')

    def __str__(self):
        return '{} - {}'.format(self.member, self.parokia)


