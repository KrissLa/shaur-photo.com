# Generated by Django 3.0.1 on 2020-01-04 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums1', '0002_auto_20200103_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotoset',
            name='description',
            field=models.TextField(default='', verbose_name='Короткое описание (для главной)'),
        ),
        migrations.AddField(
            model_name='fotoset',
            name='description1',
            field=models.TextField(default='', verbose_name='Короткое описание (для главной)'),
        ),
        migrations.AddField(
            model_name='fotoset',
            name='description2',
            field=models.TextField(default='', verbose_name='Короткое описание (для главной)'),
        ),
        migrations.AddField(
            model_name='fotoset',
            name='description3',
            field=models.TextField(default='', verbose_name='Короткое описание (для главной)'),
        ),
        migrations.AddField(
            model_name='fotoset',
            name='description4',
            field=models.TextField(default='', verbose_name='Короткое описание (для главной)'),
        ),
        migrations.AddField(
            model_name='fotoset',
            name='description5',
            field=models.TextField(default='', verbose_name='Короткое описание (для главной)'),
        ),
        migrations.AddField(
            model_name='fotoset',
            name='description6',
            field=models.TextField(default='', verbose_name='Короткое описание (для главной)'),
        ),
    ]
