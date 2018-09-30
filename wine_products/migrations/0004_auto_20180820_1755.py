# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wine_products', '0003_auto_20180820_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='code',
        ),
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
