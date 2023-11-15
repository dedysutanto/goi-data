from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
#from django_google_maps import fields as map_fields
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from data_support.models import Pekerjaan, Pendidikan


"""
@receiver(post_save, sender=Klerus)
def auto_create_member(sender, instance, created, **kwargs):
    if created:
        member = Member(name=instance.name)
        member.baptis_name = instance.baptis_name
        member.save()
"""

GENDER = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan')
        )


class Member(models.Model):
    uuid = models.UUIDField(editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Nama Lengkap'))
    dob = models.DateField(null=True, blank=True, verbose_name=_('Tanggal Lahir'))
    pob = models.CharField(max_length=50, blank=True, verbose_name=_('Tempat Lahir'))
    father = models.CharField(max_length=50, blank=True, verbose_name=_('Nama Ayah'))
    mother = models.CharField(max_length=50, blank=True, verbose_name=_('Nama Ibu'))
    gender = models.CharField(max_length=5, choices=GENDER, verbose_name=_('Jenis Kelamin'))

    photo = models.ImageField(blank=True, upload_to='member', verbose_name='Photo')
    photo_thumbnail = ImageSpecField(source='photo',
                                      processors=[ResizeToFill(60, 90)],
                                      format='JPEG',
                                      options={'quality': 60})

    email = models.EmailField(max_length=50, blank=True, verbose_name='Alamat Email')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Telpon/HP')
    address = models.CharField(max_length=250, blank=True, verbose_name='Alamat')
    geolocation = models.CharField(max_length=250, blank=True, verbose_name='Koordinat GoogleMap')
    #address = map_fields.AddressField(max_length=300, blank=True, verbose_name='Alamat')
    #geolocation = map_fields.GeoLocationField(max_length=100, blank=True, verbose_name='Koordinat GoogleMap')

    pendidikan = models.ForeignKey(
            Pendidikan,
            on_delete=models.SET_NULL,
            verbose_name=_('Pendidikan'),
            blank=True,
            null=True
            )
    pekerjaan = models.ForeignKey(
            Pekerjaan,
            on_delete=models.SET_NULL,
            verbose_name=_('Pekerjaan'),
            blank=True,
            null=True
            )

    is_alive = models.BooleanField(default=True, verbose_name='Masih Hidup')
    is_klerus = models.BooleanField(default=False, verbose_name='Klerus')
    jabatan_klerus = models.CharField(max_length=20, blank=True, verbose_name='Jabatan Klerus')
    description = models.TextField(blank=True, verbose_name='Catatan')

    baptis_number = models.CharField(max_length=30, verbose_name='Nomor Sertifikat Baptis', blank=True, null=True)
    baptis_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nama Baptis')
    baptis_klerus_id = models.IntegerField(default=0)
    baptis_klerus = models.CharField(max_length=100, blank=True, null=True, verbose_name='Klerus Yang Membaptis')
    baptis_parent_id = models.IntegerField(default=0)
    baptis_parent = models.CharField(max_length=100, blank=True, null=True, verbose_name='Orang Tua Baptis')
    baptis_anniversary = models.DateField(null=True, blank=True, verbose_name='Tanggal Peringatan')
    baptis_date = models.DateField(null=True, blank=True, verbose_name='Tanggal Baptis')
    is_baptis = models.BooleanField(default=False, verbose_name=_('Sudah Baptis'))
    #is_baptis_name_from_name = models.BooleanField(_('Nama baptis diambil dari nama asli'), default=False)

    parokia_id = models.IntegerField(default=0)
    parokia = models.CharField(max_length=100, blank=True, null=True, verbose_name='Parokia')
    komox_id = models.IntegerField(default=0)
    komox = models.CharField(max_length=100, blank=True, null=True, verbose_name='Komox')

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'member'
        verbose_name = 'Anggota'
        verbose_name_plural = 'Daftar Anggota'

    def __str__(self):
        if self.is_klerus:
            complete_name = '%s %s %s' % (self.jabatan_klerus, self.baptis_name, self.name)
        else:
            if self.baptis_name is not None:
                if self.baptis_name in self.name:
                    complete_name = '%s' % (self.name)
                else:
                    complete_name = '%s %s' % (self.baptis_name, self.name)
            else:
                complete_name = '%s' % (self.name)

        if not self.is_alive:
            complete_name = '{} (ALM)'.format(complete_name)

        return complete_name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        if self.father is not None:
            self.father = self.father.upper()
        if self.mother is not None:
            self.mother = self.mother.upper()
        if self.pob is not None:
            self.pob = self.pob.upper()

        if self.baptis_name is not None:
            self.baptis_name = self.baptis_name.upper()

        return super(Member, self).save(*args, **kwargs)


