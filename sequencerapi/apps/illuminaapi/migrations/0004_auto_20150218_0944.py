# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('illuminaapi', '0003_auto_20150218_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyze',
            name='csv',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='analyze',
            name='url',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
