# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_auto_20150602_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='koina',
            name='site',
            field=models.ForeignKey(to='sites.Site', null=True),
            preserve_default=True,
        ),
    ]
