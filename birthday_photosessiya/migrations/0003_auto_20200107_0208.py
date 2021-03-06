# Generated by Django 3.0.1 on 2020-01-06 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_photosessiya', '0002_auto_20200106_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto_birt',
            name='album',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='birthday_photosessiya.Album_birt', verbose_name='Альбом'),
        ),
        migrations.AlterField(
            model_name='foto_birt',
            name='image',
            field=models.ImageField(upload_to='birthday_photosessiya/albums', verbose_name='Фотография'),
        ),
    ]
