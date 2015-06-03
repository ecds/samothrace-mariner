# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('inscription_id', models.CharField(max_length=10, serialize=False, verbose_name=b'Inscription ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255, blank=True)),
                ('alt_name', models.CharField(max_length=255, blank=True)),
                ('start_date', models.IntegerField(max_length=4, null=True, blank=True)),
                ('end_date', models.IntegerField(max_length=4, null=True, blank=True)),
                ('date_info', models.CharField(max_length=255, blank=True)),
                ('picture', models.ImageField(null=True, upload_to=b'inscriptions', blank=True)),
                ('incription_text', models.TextField(blank=True)),
                ('bibliography', models.TextField(blank=True)),
                ('comments', models.TextField(blank=True)),
                ('dating_certainty', models.TextField(blank=True)),
                ('start_date_CE', models.IntegerField(max_length=4, null=True, blank=True)),
                ('end_date_CE', models.IntegerField(max_length=4, null=True, blank=True)),
            ],
            options={
                'ordering': ['inscription_id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReferenceSite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inscription', models.ForeignKey(to='inscriptions.Inscription')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
