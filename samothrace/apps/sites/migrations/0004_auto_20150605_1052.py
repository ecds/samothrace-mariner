# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_auto_20150603_1214'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='koina',
            options={'verbose_name_plural': 'Koina'},
        ),
        migrations.AddField(
            model_name='site',
            name='paragraph',
            field=tinymce.models.HTMLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='site',
            name='caption',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
