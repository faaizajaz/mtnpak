# Generated by Django 2.1.2 on 2018-10-19 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route',
            old_name='r_crag',
            new_name='rcrag',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='r_description',
            new_name='rdescription',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='r_name',
            new_name='rname',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='r_opener',
            new_name='ropener',
        ),
    ]
