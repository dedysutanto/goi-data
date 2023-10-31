# Generated by Django 4.2.6 on 2023-10-31 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nama Lengkap')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Tanggal Lahir')),
                ('pob', models.CharField(blank=True, max_length=50, verbose_name='Tempat Lahir')),
                ('father', models.CharField(blank=True, max_length=50, verbose_name='Nama Ayah')),
                ('mother', models.CharField(blank=True, max_length=50, verbose_name='Nama Ibu')),
                ('gender', models.CharField(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], max_length=5, verbose_name='Jenis Kelamin')),
                ('photo', models.ImageField(blank=True, upload_to='member', verbose_name='Photo')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='Alamat Email')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Telpon/HP')),
                ('address', models.CharField(blank=True, max_length=250, verbose_name='Alamat')),
                ('geolocation', models.CharField(blank=True, max_length=250, verbose_name='Koordinat GoogleMap')),
                ('is_alive', models.BooleanField(default=True, verbose_name='Masih Hidup')),
                ('is_klerus', models.BooleanField(default=False, verbose_name='Klerus')),
                ('jabatan_klerus', models.CharField(blank=True, max_length=20, verbose_name='Jabatan Klerus')),
                ('description', models.TextField(blank=True, verbose_name='Catatan')),
                ('baptis_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nomor Sertifikat Baptis')),
                ('baptis_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nama Baptis')),
                ('baptis_anniversary', models.DateField(blank=True, null=True, verbose_name='Tanggal Peringatan')),
                ('baptis_date', models.DateField(blank=True, null=True, verbose_name='Tanggal Baptis')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Anggota',
                'verbose_name_plural': 'Daftar Anggota',
                'db_table': 'member',
            },
        ),
    ]
