# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='cl_op_balance',
            new_name='stock',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='stoct_of_products',
        ),
    ]
