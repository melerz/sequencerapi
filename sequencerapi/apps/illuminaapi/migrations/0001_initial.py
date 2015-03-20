# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.illuminaapi.models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analyze',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('csv', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200, blank=True)),
                ('status', models.CharField(default=apps.illuminaapi.models.get_status, max_length=200)),
                ('configuration', jsonfield.fields.JSONField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Illumina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='analyze',
            name='illumina',
            field=models.ForeignKey(related_name='analyzes', to='illuminaapi.Illumina'),
            preserve_default=True,
        ),
    ]
