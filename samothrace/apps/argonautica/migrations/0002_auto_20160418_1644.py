# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argonautica', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['name'], 'verbose_name_plural': 'People'},
        ),
        migrations.AlterModelOptions(
            name='places_referenced',
            options={'ordering': ['line_number'], 'verbose_name': 'Place Referenced', 'verbose_name_plural': 'Places Referenced'},
        ),
        migrations.AlterModelOptions(
            name='stops',
            options={'ordering': ['line_number'], 'verbose_name': 'Sequence Stop', 'verbose_name_plural': 'Stops'},
        ),
        migrations.RemoveField(
            model_name='stops',
            name='crew',
        ),
        migrations.AddField(
            model_name='stops',
            name='crew',
            field=models.ManyToManyField(help_text=b'People on the Ship Manifest at the time', related_name='crew', null=True, to='argonautica.Person', blank=True),
        ),
    ]
