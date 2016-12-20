# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argonautica', '0005_auto_20160425_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='source',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'Apollonius of Rhodes', b'Apollonius of Rhodes'), (b'[Orpheus]', b'[Orpheus]'), (b'Valerius Flaccus', b'Valerius Flaccus')]),
        ),
        migrations.AlterField(
            model_name='places_referenced',
            name='argonautica_edition',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'Apollonius of Rhodes', b'Apollonius of Rhodes'), (b'[Orpheus]', b'[Orpheus]'), (b'Valerius Flaccus', b'Valerius Flaccus')]),
        ),
        migrations.AlterField(
            model_name='stops',
            name='argonautica_edition',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'Apollonius of Rhodes', b'Apollonius of Rhodes'), (b'[Orpheus]', b'[Orpheus]'), (b'Valerius Flaccus', b'Valerius Flaccus')]),
        ),
        migrations.AlterField(
            model_name='stops',
            name='next_place',
            field=models.ForeignKey(related_name='next', blank=True, to='sites.Site', null=True),
        ),
        migrations.AlterField(
            model_name='stops',
            name='previous_place',
            field=models.ForeignKey(related_name='previous', blank=True, to='sites.Site', null=True),
        ),
    ]
