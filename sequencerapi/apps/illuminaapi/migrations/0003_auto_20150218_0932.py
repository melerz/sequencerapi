# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('illuminaapi', '0002_remove_run_sheker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='illumina',
            name='date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
