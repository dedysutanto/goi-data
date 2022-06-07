from django.db import models
from django_google_maps import fields as map_fields
from klerus.models import Klerus
from member.models import Member


class Parokia(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nama Parokia')
    code = models.CharField(max_length=10, unique=True, verbose_name='Kode Parokia')
    address = map_fields.AddressField(max_length=200, blank=True, verbose_name='Alamat')
    geolocation = map_fields.GeoLocationField(max_length=100, blank=True, verbose_name='Koordinat GoogleMap')
    email = models.EmailField(max_length=20, blank=True, verbose_name='Alamat Email')
    phone = models.CharField(max_length=20, verbose_name='Telpon/HP', blank=True)
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
        return super(Parokia, self).save(*args, **kwargs)


class Komox(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nama Komox')
    code = models.CharField(max_length=10, unique=True, verbose_name='Kode Komox')
    address = map_fields.AddressField(max_length=200, blank=True, verbose_name='Alamat')
    geolocation = map_fields.GeoLocationField(max_length=100, blank=True, verbose_name='Koordinat GoogleMap')
    email = models.EmailField(max_length=20, blank=True, verbose_name='Alamat Email')
    phone = models.CharField(max_length=20, verbose_name='Telpon/HP', blank=True)
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
        return super(Komox, self).save(*args, **kwargs)

