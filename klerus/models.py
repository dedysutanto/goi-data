from django.db import models
from member.models import Member
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import gettext_lazy as _


JABATAN_KLERUS = (
    ('ROMOEPISKOP', 'ROMO EPISKOP'),
    ('ROMO', 'ROMO'),
    ('ROMODIAKON', 'ROMO DIAKON'),
    ('SUBDIAKEN', 'SUB-DIAKEN'),
)


class JabatanKlerus(models.Model):
    name = models.CharField(_('Nama Jabatan'), max_length=100)

    class Meta:
        db_table = 'jabatan_klerus'
        verbose_name = 'Jabatan Klerus'
        verbose_name_plural = 'Jabatan Klerus'

    def __str__(self):
        return '{}'.format(self.name)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.name = self.name.upper()
        return super(JabatanKlerus, self).save(force_insert, force_update, using, update_fields)

class Klerus(models.Model):
    #jabatan = models.CharField(max_length=20, choices=JABATAN_KLERUS,
    #                           default='ROMO', verbose_name='Jabatan Klerus')
    jabatan = models.ForeignKey(
            JabatanKlerus,
            on_delete=models.RESTRICT,
            verbose_name=_('Jabatan')
            )

    name = models.ForeignKey(
        Member,
        on_delete=models.RESTRICT,
        verbose_name=_('Name Klerus')
    )

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    class Meta:
        db_table = 'klerus'
        verbose_name = 'Klerus'
        verbose_name_plural = 'Daftar Klerus'
        
    def __str__(self):
        return '%s %s %s' % (self.jabatan, self.name.baptis_name, self.name.name)

    def save(self, *args, **kwargs):
        try:
            member = Member.objects.get(id=self.name.id)
            member.is_klerus = True
            member.jabatan_klerus = self.jabatan.name
            member.save()

        except ObjectDoesNotExist:
            pass

        return super(Klerus, self).save(*args, **kwargs)
