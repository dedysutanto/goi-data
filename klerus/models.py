from django.db import models
from member.models import Member
from django.core.exceptions import ObjectDoesNotExist, ValidationError


JABATAN_KLERUS = (
    ('ROMO', 'ROMO'),
    ('ROMODIAKON', 'ROMO DIAKON'),
    ('SUBDIAKEN', 'SUB-DIAKEN'),
)


class Klerus(models.Model):
    jabatan = models.CharField(max_length=20, choices=JABATAN_KLERUS,
                               default='ROMO', verbose_name='Jabatan Klerus')
    name = models.ForeignKey(
        Member,
        on_delete=models.RESTRICT,
        verbose_name='Name Klerus'
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
            member.jabatan_klerus = self.jabatan
            member.save()

        except ObjectDoesNotExist:
            pass

        return super(Klerus, self).save(*args, **kwargs)
