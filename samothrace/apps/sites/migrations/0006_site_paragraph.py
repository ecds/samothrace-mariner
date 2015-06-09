# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0005_remove_site_paragraph'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='paragraph',
            field=tinymce.models.HTMLField(blank=True),
            preserve_default=True,
        ),
    ]
