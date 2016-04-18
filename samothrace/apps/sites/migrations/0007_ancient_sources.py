# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0006_site_paragraph'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ancient_Sources',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=255, null=True, blank=True)),
                ('reference', models.CharField(help_text=b'Text and section', max_length=255, null=True, blank=True)),
                ('author_date', models.CharField(max_length=255, null=True, blank=True)),
                ('language', models.CharField(max_length=255, null=True, blank=True)),
                ('citation_url', models.URLField(null=True, blank=True)),
                ('bibliographic_reference', models.CharField(help_text=b"Sources without available URL's", max_length=255, null=True, blank=True)),
                ('cityname', models.ForeignKey(db_column=b'name', blank=True, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Ancient Source',
                'verbose_name_plural': 'Ancient Sources',
            },
        ),
    ]
