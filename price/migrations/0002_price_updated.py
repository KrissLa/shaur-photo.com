# Generated by Django 3.0.2 on 2020-01-11 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
