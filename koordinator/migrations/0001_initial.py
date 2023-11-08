# Generated by Django 4.2.6 on 2023-11-02 10:06

from django.db import migrations, models
import django.db.models.deletion
import koordinator.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('klerus', '0001_initial'),
        ('parokia', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParokiaKlerus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klerus', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='klerus.klerus', verbose_name='Klerus')),
                ('parokia', models.ForeignKey(limit_choices_to=koordinator.models.ParokiaKlerus.limit_choice_to_parokia, on_delete=django.db.models.deletion.RESTRICT, to='parokia.parokia', verbose_name='Parokia')),
            ],
            options={
                'verbose_name': 'Parokia Klerus',
                'verbose_name_plural': 'Parokia Klerus',
                'db_table': 'parokia_klerus',
            },
        ),
        migrations.CreateModel(
            name='KomoxKoordinator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('komox', models.ForeignKey(limit_choices_to=koordinator.models.KomoxKoordinator.limit_choice_to_komox, on_delete=django.db.models.deletion.RESTRICT, to='parokia.komox', verbose_name='Komunitas Orthodox')),
                ('koordinator', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='member.member', verbose_name='Koordinator')),
            ],
            options={
                'verbose_name': 'Komox Koordinator',
                'verbose_name_plural': 'Komox Koordinator',
                'db_table': 'komox_koordinator',
            },
        ),
    ]