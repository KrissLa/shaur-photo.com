# Generated by Django 3.0.1 on 2020-01-03 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('individualnaya_photosessiya', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto_ind',
            name='image',
            field=models.ImageField(upload_to='individualnaya_fotosessiya/albums', verbose_name='Фотография'),
        ),
    ]
