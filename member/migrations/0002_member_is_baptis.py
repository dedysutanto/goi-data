# Generated by Django 4.2.6 on 2023-11-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_baptis',
            field=models.BooleanField(default=False),
        ),
    ]
