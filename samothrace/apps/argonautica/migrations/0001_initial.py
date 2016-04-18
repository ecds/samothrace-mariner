# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0008_site_natural_marker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('tribe', models.CharField(max_length=255, null=True, blank=True)),
                ('origin', models.ForeignKey(blank=True, to='sites.Site', null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Places_Referenced',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('line_number', models.CharField(max_length=255, null=True, blank=True)),
                ('type_of_reference', models.CharField(max_length=255, null=True, blank=True)),
                ('ritual', models.CharField(max_length=255, null=True, blank=True)),
                ('ritual_deity', models.CharField(max_length=255, null=True, blank=True)),
                ('next_place', models.ForeignKey(related_name='next2', blank=True, to='sites.Site')),
                ('place_referenced', models.ForeignKey(related_name='ref', blank=True, to='sites.Site')),
                ('previous_place', models.ForeignKey(related_name='previous2', blank=True, to='sites.Site')),
                ('referenced_by', models.ForeignKey(related_name='speaking', blank=True, to='argonautica.Person', help_text=b'Person making the place reference', null=True)),
                ('ritual_people', models.ForeignKey(related_name='ritualpeople2', blank=True, to='argonautica.Person', help_text=b'People associated with the ritual', null=True)),
            ],
            options={
                'ordering': ['line_number'],
            },
        ),
        migrations.CreateModel(
            name='Stops',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_of_stop', models.CharField(blank=True, max_length=255, null=True, choices=[(b'direct', b'direct'), (b'indirect', b'indirect')])),
                ('line_number', models.CharField(max_length=255, null=True, blank=True)),
                ('ritual', models.CharField(max_length=255, null=True, blank=True)),
                ('ritual_deity', models.CharField(max_length=255, null=True, blank=True)),
                ('crew', models.ForeignKey(related_name='crew', blank=True, to='argonautica.Person', help_text=b'People on the Ship Manifest at the time', null=True)),
                ('next_place', models.ForeignKey(related_name='next', blank=True, to='sites.Site')),
                ('place_of_stop', models.ForeignKey(related_name='stop', blank=True, to='sites.Site')),
                ('previous_place', models.ForeignKey(related_name='previous', blank=True, to='sites.Site')),
                ('ritual_people', models.ForeignKey(related_name='ritualpeople', blank=True, to='argonautica.Person', help_text=b'People associated with the ritual', null=True)),
            ],
            options={
                'ordering': ['line_number'],
            },
        ),
    ]
