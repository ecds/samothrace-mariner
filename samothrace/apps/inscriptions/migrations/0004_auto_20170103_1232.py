# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0010_auto_20170103_1232'),
        ('inscriptions', '0003_auto_20150608_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_of_people', models.IntegerField(null=True, blank=True)),
                ('inscription', models.CharField(max_length=255, null=True, blank=True)),
                ('inscription_text', models.TextField(null=True, blank=True)),
                ('bibliographic', models.CharField(help_text=b'List Mack pages.', max_length=255, null=True, blank=True)),
                ('date_range', models.CharField(max_length=255, null=True, blank=True)),
                ('date_begin', models.IntegerField(null=True, blank=True)),
                ('date_end', models.IntegerField(null=True, blank=True)),
                ('inscriptionlink', tinymce.models.HTMLField(null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('granting_name', models.ForeignKey(related_name='granting', to='sites.Site')),
                ('receiving_name', models.ForeignKey(related_name='receiving', to='sites.Site')),
            ],
        ),
        migrations.AlterField(
            model_name='inscription',
            name='end_date',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='end_date_CE',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='start_date',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='start_date_CE',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
