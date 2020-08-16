# Generated by Django 3.0.7 on 2020-07-17 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crags', '0006_auto_20200717_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crag',
            name='cauthor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Page author'),
        ),
    ]