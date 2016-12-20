# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0008_site_natural_marker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='alt_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='caption',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='mod_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='natural_marker',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='paragraph',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='perseus_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='pleiades_url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
