# Generated by Django 3.0.8 on 2020-07-31 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0003_auto_20200731_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='rdescription',
            field=models.CharField(max_length=10000, verbose_name='Route Description'),
        ),
    ]
