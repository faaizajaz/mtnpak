# Generated by Django 3.0.8 on 2020-08-09 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crags', '0010_crag_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='crag',
            name='toprope',
            field=models.CharField(default='No information', max_length=50, verbose_name='Top rope access'),
            preserve_default=False,
        ),
    ]