# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0004_auto_20150605_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='paragraph',
        ),
    ]
