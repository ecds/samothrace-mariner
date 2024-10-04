# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argonautica', '0004_remove_person_tribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='places_referenced',
            name='argonautica_edition',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4')]),
        ),
        migrations.AddField(
            model_name='stops',
            name='argonautica_edition',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4')]),
        ),
    ]
