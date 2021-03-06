# Generated by Django 4.0.5 on 2022-06-06 03:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('klerus', '0002_alter_klerus_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='klerus',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klerus',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='klerus',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nama Lengkap Klerus'),
        ),
    ]
