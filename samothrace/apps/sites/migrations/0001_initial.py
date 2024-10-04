# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Koina',
            fields=[
                ('koina_id', models.CharField(max_length=10, serialize=False, verbose_name=b'Koina ID', primary_key=True)),
                ('member_count', models.IntegerField(max_length=4, null=True, blank=True)),
                ('activities', models.CharField(max_length=255, blank=True)),
                ('comments', models.TextField(blank=True)),
                ('inscription', models.ForeignKey(to='inscriptions.Inscription')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('marker_id', models.CharField(max_length=10, serialize=False, verbose_name=b'Marker ID', primary_key=True)),
                ('type', models.CharField(max_length=255, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('site_id', models.CharField(max_length=10, serialize=False, verbose_name=b'Site ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('mod_name', models.CharField(max_length=255, blank=True)),
                ('alt_name', models.CharField(max_length=255, blank=True)),
                ('latitude', models.DecimalField(null=True, max_digits=9, decimal_places=6, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=9, decimal_places=6, blank=True)),
                ('elevation', models.IntegerField(max_length=4, null=True, blank=True)),
                ('pleiades_url', models.URLField(blank=True)),
                ('perseus_url', models.URLField(blank=True)),
                ('caption', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['site_id'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='site',
            unique_together=set([('latitude', 'longitude')]),
        ),
        migrations.AddField(
            model_name='marker',
            name='site',
            field=models.ForeignKey(to='sites.Site'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='koina',
            name='site',
            field=models.ForeignKey(to='sites.Site'),
            preserve_default=True,
        ),
    ]
