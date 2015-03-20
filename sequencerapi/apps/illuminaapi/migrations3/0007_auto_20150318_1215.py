# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.illuminaapi.models


class Migration(migrations.Migration):

    dependencies = [
        ('illuminaapi', '0006_auto_20150318_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyze',
            name='status',
            field=models.CharField(default=apps.illuminaapi.models.get_status, max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
