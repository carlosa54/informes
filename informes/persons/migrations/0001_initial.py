# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('regional', models.CharField(default=b'sanjuan', max_length=50, choices=[(b'arecibo', b'arecibo'), (b'bayamon', b'bayamon'), (b'caguas', b'caguas'), (b'mayaguez', b'mayaguez'), (b'ponce', b'ponce'), (b'sanjuan', b'sanjuan')])),
            ],
            options={
                'ordering': ('-modified_at', '-created_at'),
                'abstract': False,
                'get_latest_by': 'modified_at',
            },
            bases=(models.Model,),
        ),
    ]
