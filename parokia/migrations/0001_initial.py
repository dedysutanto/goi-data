# Generated by Django 4.2.6 on 2023-11-02 10:06

from django.db import migrations, models
import django.db.models.deletion
import parokia.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('klerus', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Komox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nama Komox')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='Kode Komox')),
                ('address', models.CharField(blank=True, max_length=250, verbose_name='Alamat')),
                ('geolocation', models.CharField(blank=True, max_length=250, verbose_name='Koordinat GoogleMap')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='Alamat Email')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Telpon/HP')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('klerus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='klerus.klerus', verbose_name='Klerus')),
            ],
            options={
                'verbose_name': 'Komunitas Orthodox',
                'verbose_name_plural': 'Daftar Komox',
                'db_table': 'komox',
            },
        ),
        migrations.CreateModel(
            name='Parokia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nama Parokia')),
                ('code', models.CharField(help_text='Kode Parokia bisa menggunakan singkatan. Contoh: JSPP untuk Js Petrus dan Paulus', max_length=20, unique=True, verbose_name='Kode Parokia')),
                ('address', models.CharField(blank=True, max_length=250, verbose_name='Alamat')),
                ('geolocation', models.CharField(blank=True, max_length=250, verbose_name='Koordinat GoogleMap')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='Alamat Email')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Telpon/HP')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Parokia',
                'verbose_name_plural': 'Daftar Parokia',
                'db_table': 'parokia',
            },
        ),
        migrations.CreateModel(
            name='MemberParokia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('komox', models.ForeignKey(blank=True, limit_choices_to=parokia.models.MemberParokia.limit_choices_to_parokia, null=True, on_delete=django.db.models.deletion.CASCADE, to='parokia.komox', verbose_name='Komox')),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='member.member', verbose_name='Anggota')),
                ('parokia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parokia.parokia', verbose_name='Parokia')),
            ],
            options={
                'verbose_name': 'Anggota Parokia dan Komox',
                'verbose_name_plural': 'Anggota Parokia dan Komox',
                'db_table': 'member_parokia',
            },
        ),
        migrations.AddField(
            model_name='komox',
            name='parokia',
            field=models.ForeignKey(limit_choices_to=parokia.models.Komox.limit_choices_to_parokia, on_delete=django.db.models.deletion.RESTRICT, related_name='parokia_komox', to='parokia.parokia', verbose_name='Parokia'),
        ),
    ]
