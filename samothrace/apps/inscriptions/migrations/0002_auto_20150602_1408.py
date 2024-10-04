# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('inscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='referencesite',
            name='site',
            field=models.ForeignKey(to='sites.Site'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inscription',
            name='find_spot',
            field=models.ForeignKey(to='sites.Site'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inscription',
            name='sites_mentioned',
            field=models.ManyToManyField(related_name='sites_mentioned', null=True, through='inscriptions.ReferenceSite', to='sites.Site', blank=True),
            preserve_default=True,
        ),
    ]
