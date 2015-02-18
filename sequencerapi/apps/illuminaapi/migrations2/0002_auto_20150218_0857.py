# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('illuminaapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyze',
            name='run_id',
            field=models.ForeignKey(to='illuminaapi.Run'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='run',
            name='illumina_id',
            field=models.ForeignKey(to='illuminaapi.Illumina'),
            preserve_default=True,
        ),
    ]
