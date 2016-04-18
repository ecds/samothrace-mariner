# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0007_ancient_sources'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='natural_marker',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
