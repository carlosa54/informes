# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(unique=True, max_length=45)),
                ('email', models.EmailField(unique=True, max_length=40)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('regional', models.CharField(default=b'sanjuan', max_length=50, choices=[(b'arecibo', b'arecibo'), (b'bayamon', b'bayamon'), (b'caguas', b'caguas'), (b'mayaguez', b'mayaguez'), (b'ponce', b'ponce'), (b'sanjuan', b'sanjuan')])),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-modified_at', '-created_at'),
                'abstract': False,
                'get_latest_by': 'modified_at',
            },
            bases=(models.Model,),
        ),
    ]
