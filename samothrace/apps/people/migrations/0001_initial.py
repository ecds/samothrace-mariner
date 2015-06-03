# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('inscriptions', '0002_auto_20150602_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('individual_id', models.CharField(max_length=10, serialize=False, verbose_name=b'Individual ID', primary_key=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('patronym', models.CharField(max_length=255, blank=True)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('comments', models.TextField(blank=True)),
                ('inscription', models.ForeignKey(to='inscriptions.Inscription')),
                ('site', models.ForeignKey(blank=True, to='sites.Site', null=True)),
                ('site_origin', models.ForeignKey(related_name='site_origin', blank=True, to='sites.Site', null=True)),
            ],
            options={
                'ordering': ['name', 'patronym'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Priesthood',
            fields=[
                ('priesthood_id', models.CharField(max_length=255, serialize=False, verbose_name=b'Priesthood ID', primary_key=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('deity_id', models.CharField(max_length=10, blank=True)),
                ('deity', models.CharField(max_length=255, blank=True)),
                ('duration', models.CharField(max_length=255, blank=True)),
                ('att_honor', models.CharField(max_length=255, blank=True)),
                ('cer_ritual', models.CharField(max_length=255, blank=True)),
                ('comments', models.TextField(blank=True)),
                ('inscription', models.ManyToManyField(to='inscriptions.Inscription', null=True, blank=True)),
                ('location', models.ForeignKey(to='sites.Site')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.CharField(max_length=10, serialize=False, verbose_name=b'Role ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('comments', models.TextField(blank=True)),
                ('individual', models.ForeignKey(to='people.Individual')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='priesthood',
            name='role',
            field=models.ForeignKey(blank=True, to='people.Role', null=True),
            preserve_default=True,
        ),
    ]
