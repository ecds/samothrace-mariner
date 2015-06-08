# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0002_auto_20150602_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscription',
            old_name='incription_text',
            new_name='inscription_text',
        ),
    ]
