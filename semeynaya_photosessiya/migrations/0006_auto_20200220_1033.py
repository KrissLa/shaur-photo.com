# Generated by Django 3.0.1 on 2020-02-20 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semeynaya_photosessiya', '0005_auto_20200215_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto_sem',
            name='image_low',
            field=models.ImageField(default='#', upload_to='semeynaya_photosessiya/albums/low', verbose_name='Сжатая фотография'),
        ),
        migrations.AlterField(
            model_name='foto_sem',
            name='image',
            field=models.ImageField(blank=True, upload_to='semeynaya_photosessiya/albums', verbose_name='Фотография хорошего качества'),
        ),
    ]
