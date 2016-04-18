# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_remove_individual_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priesthood',
            name='inscription',
            field=models.ManyToManyField(to='inscriptions.Inscription', blank=True),
        ),
    ]
