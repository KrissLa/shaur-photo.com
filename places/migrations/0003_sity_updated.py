# Generated by Django 3.0.2 on 2020-01-11 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20191229_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='sity',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
