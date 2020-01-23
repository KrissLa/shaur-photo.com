# Generated by Django 3.0.2 on 2020-01-11 04:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('detskaya_photosessiya', '0002_remove_album_det_date_album'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album_det',
            options={'ordering': ('-publish',), 'verbose_name': 'Альбом', 'verbose_name_plural': 'Альбомы'},
        ),
        migrations.AddField(
            model_name='album_det',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='album_det',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
