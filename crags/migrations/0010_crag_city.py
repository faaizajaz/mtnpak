# Generated by Django 3.0.8 on 2020-08-04 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
        ('crags', '0009_auto_20200804_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='crag',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cities.City', verbose_name='City'),
            preserve_default=False,
        ),
    ]