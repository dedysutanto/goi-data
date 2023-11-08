from django.db import models

class Pendidikan(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'pendidikan'
        verbose_name_plural = 'Pendidikan'
    
    def __str__(self):
        return '%s' % self.name
 
    def clean(self):
        self.name = self.name.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Pendidikan, self).save(*args, **kwargs)


class Pekerjaan(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'pekerjaan'
        verbose_name_plural = 'pekerjaan'
    
    def __str__(self):
        return '%s' % self.name
 
    def clean(self):
        self.name = self.name.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Pekerjaan, self).save(*args, **kwargs)


class Nob(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'nob'
        verbose_name_plural = 'Nature Of Business'
    
    def __str__(self):
        return '%s' % self.name

    def clean(self):
        self.name = self.name.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Nob, self).save(*args, **kwargs)

# https://en.wikipedia.org/wiki/Ethnic_groups_in_Indonesia
class Etnik(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'etnik'
        verbose_name_plural = 'Etnik'

    def __str__(self):
        return '%s' % self.name

    def clean(self):
        self.name = self.name.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Etnik, self).save(*args, **kwargs)

