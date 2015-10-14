# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informesmen', '0004_informe_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informe',
            name='questions',
            field=models.ManyToManyField(to='departamentos.Answer', through='informesmen.InformeQuestion'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='informequestion',
            name='question',
            field=models.ForeignKey(to='departamentos.Answer'),
            preserve_default=True,
        ),
    ]
