# Generated by Django 3.0.1 on 2020-02-20 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('svadebnaya_fotosessiya', '0007_auto_20200220_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='image_low',
            field=models.ImageField(default='Это поле обязательно к заполнению', upload_to='svadebnaya_fotosessiya/albums/low', verbose_name='Сжатая фотография'),
        ),
    ]