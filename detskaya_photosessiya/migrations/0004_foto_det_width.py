# Generated by Django 3.0.1 on 2020-02-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detskaya_photosessiya', '0003_auto_20200111_0415'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto_det',
            name='width',
            field=models.CharField(blank=True, default='стандарт', max_length=100, verbose_name='Ширина'),
        ),
    ]
