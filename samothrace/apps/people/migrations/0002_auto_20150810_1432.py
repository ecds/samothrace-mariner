# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role',
            options={'ordering': ['title']},
        ),
        migrations.RenameField(
            model_name='role',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='role',
            name='certainty',
            field=models.DecimalField(default=Decimal('0'), help_text=b'Enter a value between 0 and 1.', verbose_name=b'certainty', max_digits=3, decimal_places=2),
            preserve_default=True,
        ),
    ]
