# Generated by Django 3.0.7 on 2020-07-17 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ggrade', models.CharField(blank=True, max_length=10, verbose_name='French Grade')),
                ('ydsgrade', models.CharField(blank=True, max_length=10, verbose_name='YDS Grade')),
                ('ausgrade', models.CharField(blank=True, max_length=10, verbose_name='Ewbanks Grade')),
                ('uiaagrade', models.CharField(blank=True, max_length=10, verbose_name='UIAA Grade')),
                ('sagrade', models.CharField(blank=True, max_length=10, verbose_name='SA Grade')),
                ('ukgrade', models.CharField(blank=True, max_length=10, verbose_name='UK Grade')),
            ],
        ),
    ]
