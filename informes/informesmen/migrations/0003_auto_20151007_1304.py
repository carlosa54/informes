# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informesmen', '0002_auto_20151007_1250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informe',
            old_name='question',
            new_name='questions',
        ),
    ]
