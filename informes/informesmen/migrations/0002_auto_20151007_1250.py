# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0001_initial'),
        ('informesmen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformeQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('informe', models.ForeignKey(to='informesmen.Informe')),
                ('question', models.ForeignKey(to='departamentos.DepartamentoQuestion')),
            ],
            options={
                'ordering': ('-modified_at', '-created_at'),
                'abstract': False,
                'get_latest_by': 'modified_at',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='informe',
            name='question',
            field=models.ManyToManyField(to='departamentos.DepartamentoQuestion', through='informesmen.InformeQuestion'),
            preserve_default=True,
        ),
    ]
