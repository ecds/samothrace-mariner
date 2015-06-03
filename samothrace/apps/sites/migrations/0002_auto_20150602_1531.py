# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ['name']},
        ),
        migrations.AlterUniqueTogether(
            name='site',
            unique_together=set([]),
        ),
    ]
