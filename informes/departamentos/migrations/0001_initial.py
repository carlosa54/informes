# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('personas', models.ManyToManyField(to='persons.Person')),
                ('questions', models.ManyToManyField(to='questions.Question')),
            ],
            options={
                'ordering': ('-modified_at', '-created_at'),
                'abstract': False,
                'get_latest_by': 'modified_at',
            },
        ),
    ]
