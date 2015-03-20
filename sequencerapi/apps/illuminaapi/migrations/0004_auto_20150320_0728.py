# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('illuminaapi', '0003_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='analyze',
            field=models.ForeignKey(related_name='job', to='illuminaapi.Analyze'),
            preserve_default=True,
        ),
    ]
