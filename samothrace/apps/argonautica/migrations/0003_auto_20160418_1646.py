# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argonautica', '0002_auto_20160418_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places_referenced',
            name='ritual_people',
        ),
        migrations.AddField(
            model_name='places_referenced',
            name='ritual_people',
            field=models.ManyToManyField(help_text=b'People associated with the ritual', related_name='ritualpeople2', null=True, to='argonautica.Person', blank=True),
        ),
        migrations.RemoveField(
            model_name='stops',
            name='ritual_people',
        ),
        migrations.AddField(
            model_name='stops',
            name='ritual_people',
            field=models.ManyToManyField(help_text=b'People associated with the ritual', related_name='ritualpeople', null=True, to='argonautica.Person', blank=True),
        ),
    ]
