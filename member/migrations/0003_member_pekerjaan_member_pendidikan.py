# Generated by Django 4.2.6 on 2023-11-08 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_support', '0002_etnik'),
        ('member', '0002_member_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='pekerjaan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_support.pekerjaan', verbose_name='Pekerjaan'),
        ),
        migrations.AddField(
            model_name='member',
            name='pendidikan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_support.pendidikan', verbose_name='Pendidikan'),
        ),
    ]
