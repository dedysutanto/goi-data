# Generated by Django 4.2.6 on 2023-11-13 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parokia', '0002_komox_uuid_parokia_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='parokia',
            name='description',
            field=models.TextField(blank=True, verbose_name='Catatan'),
        ),
    ]
