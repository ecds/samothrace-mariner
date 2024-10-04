# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscriptions', '0004_auto_20170103_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='inscriptionlink',
            field=models.URLField(null=True, blank=True),
        ),
    ]
