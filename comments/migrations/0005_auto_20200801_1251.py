# Generated by Django 3.0.8 on 2020-08-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_auto_20200801_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='Comment body'),
        ),
    ]
