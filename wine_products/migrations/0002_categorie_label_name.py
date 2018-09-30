# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wine_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='label_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
