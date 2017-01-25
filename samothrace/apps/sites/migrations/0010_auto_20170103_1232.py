# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0009_auto_20160829_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='batlas',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Barrington Atlas', blank=True),
        ),
        migrations.AlterField(
            model_name='koina',
            name='member_count',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='elevation',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
