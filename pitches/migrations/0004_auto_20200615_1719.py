# Generated by Django 3.0.7 on 2020-06-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitches', '0003_auto_20200615_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitch',
            name='pdescription',
            field=models.TextField(blank=True, default='', verbose_name='Pitch Description'),
        ),
    ]
