# Generated by Django 2.1.2 on 2018-10-21 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ascents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ascent',
            name='date',
            field=models.DateField(),
        ),
    ]
