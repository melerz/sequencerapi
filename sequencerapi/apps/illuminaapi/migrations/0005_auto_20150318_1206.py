# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('illuminaapi', '0004_auto_20150218_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analyze',
            name='isFinished',
        ),
        migrations.AddField(
            model_name='analyze',
            name='status',
            field=models.CharField(default=b'running', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='analyze',
            name='csv',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='analyze',
            name='run_id',
            field=models.ForeignKey(related_name='analyzes', to='illuminaapi.Run'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='analyze',
            name='url',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='run',
            name='illumina_id',
            field=models.ForeignKey(related_name='runs', to='illuminaapi.Illumina'),
            preserve_default=True,
        ),
    ]
