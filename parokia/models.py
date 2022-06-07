from django.db import models
from django_google_maps import fields as map_fields
from klerus.models import Klerus


class Parokia(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nama Parokia')
    code = models.CharField(max_length=10, unique=True, verbose_name='Kode Parokia')
    address = map_fields.AddressField(max_length=200, blank=True, verbose_name='Alamat')
    geolocation = map_fields.GeoLocationField(max_length=100, blank=True, verbose_name='Koordinat GoogleMap')
    email = models.EmailField(max_length=20, blank=True, verbose_name='Alamat Email')
    phone = models.CharField(max_length=20, verbose_name='Telpon/HP', blank=True)
    klerus = models.ForeignKey(
        Klerus,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='Nama Klerus'
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


