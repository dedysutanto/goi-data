from django.db import models


class Klerus(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nama Lengkap Klerus')

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    class Meta:
        db_table = 'klerus'
        verbose_name = 'Klerus'
        verbose_name_plural = 'Daftar Klerus'
        
    def __str__(self):
        return '%s' % self.name
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super(Klerus, self).save(*args, **kwargs)
