# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argonautica', '0003_auto_20160418_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='tribe',
        ),
    ]
