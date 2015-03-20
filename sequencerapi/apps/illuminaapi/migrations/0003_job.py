# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.illuminaapi.models


class Migration(migrations.Migration):

    dependencies = [
        ('illuminaapi', '0002_auto_20150320_0208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default=apps.illuminaapi.models.get_status, max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('analyze', models.ForeignKey(related_name='analyzes', to='illuminaapi.Analyze')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
