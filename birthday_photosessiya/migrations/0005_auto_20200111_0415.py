# Generated by Django 3.0.2 on 2020-01-11 04:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_photosessiya', '0004_remove_album_birt_date_album'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album_birt',
            options={'ordering': ('-publish',), 'verbose_name': 'Альбом', 'verbose_name_plural': 'Альбомы'},
        ),
        migrations.AddField(
            model_name='album_birt',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='album_birt',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
