# Generated by Django 3.0.7 on 2020-06-17 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routetypes', '0003_auto_20200617_1825'),
        ('routes', '0005_delete_tradroute'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='rtype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='routetypes.RouteType'),
        ),
        migrations.AlterField(
            model_name='route',
            name='rlength',
            field=models.IntegerField(default=0, verbose_name='Route Length'),
        ),
    ]