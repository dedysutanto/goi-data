# Generated by Django 4.0.5 on 2022-06-07 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parokia', '0005_alter_parokia_klerus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parokia',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Telpon/HP'),
        ),
    ]
