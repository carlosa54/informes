# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('persona', models.ForeignKey(to='persons.Person')),
            ],
            options={
                'ordering': ('-modified_at', '-created_at'),
                'abstract': False,
                'get_latest_by': 'modified_at',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('-modified_at', '-created_at'),
                'abstract': False,
                'get_latest_by': 'modified_at',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DepartamentoPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('departamento', models.ForeignKey(to='departamentos.Departamento')),
                ('persona', models.ForeignKey(to='persons.Person')),
            ],
            options={
                'ordering': ('-modified_at', '-created_at'),
                'abstract': False,
                'get_latest_by': 'modified_at',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DepartamentoQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('departamento', models.ForeignKey(to='departamentos.Departamento')),
                ('question', models.ForeignKey(to='questions.Question')),
            ],
            options={
                'ordering': ('-modified_at', '-created_at'),
                'abstract': False,
                'get_latest_by': 'modified_at',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='departamento',
            name='personas',
            field=models.ManyToManyField(to='persons.Person', through='departamentos.DepartamentoPerson'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='departamento',
            name='questions',
            field=models.ManyToManyField(to='questions.Question', through='departamentos.DepartamentoQuestion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='pregunta',
            field=models.ForeignKey(to='departamentos.DepartamentoQuestion'),
            preserve_default=True,
        ),
    ]
