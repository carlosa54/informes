# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_person_regional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='regional',
            field=models.CharField(default=b'sanjuan', max_length=50, choices=[(b'arecibo', b'arecibo'), (b'bayamon', b'bayamon'), (b'caguas', b'caguas'), (b'mayaguez', b'mayaguez'), (b'ponce', b'ponce'), (b'sanjuan', b'sanjuan')]),
        ),
    ]
