from django.db import models
from klerus.models import Klerus
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_google_maps import fields as map_fields
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


@receiver(post_save, sender=Klerus)
def auto_create_member(sender, instance, created, **kwargs):
    if created:
        member = Member(name=instance.name)
        member.save()


class Member(models.Model):

    name = models.CharField(max_length=50, verbose_name='Nama Lengkap')
    dob = models.DateField(null=True, blank=True, verbose_name='Tanggal Lahir')
    pob = models.CharField(max_length=50, blank=True, verbose_name='Tempat Lahir')
    father = models.CharField(max_length=50, blank=True, verbose_name='Nama Ayah')
    mother = models.CharField(max_length=50, blank=True, verbose_name='Nama Ibu')

    photo = models.ImageField(blank=True, upload_to='member', verbose_name='Photo')
    photo_thumbnail = ImageSpecField(source='photo',
                                      processors=[ResizeToFill(60, 90)],
                                      format='JPEG',
                                      options={'quality': 60})

    email = models.EmailField(max_length=20, blank=True, verbose_name='Alamat Email')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Telpon/HP')
    address = map_fields.AddressField(max_length=200, blank=True, verbose_name='Alamat')
    geolocation = map_fields.GeoLocationField(max_length=100, blank=True, verbose_name='Koordinat GoogleMap')

    is_alive = models.BooleanField(default=True, verbose_name='Hidup/Almarhum')

    baptis_number = models.CharField(max_length=30, verbose_name='Nomor Sertifikat Baptis', blank=True)
    baptis_name = models.CharField(max_length=30, blank=True, verbose_name='Nama Baptis')
    baptis_anniversary = models.DateField(null=True, blank=True, verbose_name='Tanggal Peringatan')
    baptis_date = models.DateField(null=True, blank=True, verbose_name='Tanggal Baptis')

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'member'
        verbose_name = 'Anggota'
        verbose_name_plural = 'Daftar Anggota'

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        if self.father is not None:
            self.father = self.father.upper()
        if self.mother is not None:
            self.mother = self.mother.upper()
        if self.pob is not None:
            self.pob = self.pob.upper()

        return super(Member, self).save(*args, **kwargs)



