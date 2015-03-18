# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.illuminaapi.models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('illuminaapi', '0007_auto_20150318_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='analyze',
            old_name='run_id',
            new_name='run',
        ),
        migrations.RenameField(
            model_name='run',
            old_name='illumina_id',
            new_name='illumina',
        ),
        migrations.AddField(
            model_name='analyze',
            name='configuration',
            field=jsonfield.fields.JSONField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='analyze',
            name='status',
            field=models.CharField(default=apps.illuminaapi.models.get_status, max_length=200),
            preserve_default=True,
        ),
    ]
