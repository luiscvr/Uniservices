# Generated by Django 2.0.9 on 2018-12-11 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_servicio_encargado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='duracion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
