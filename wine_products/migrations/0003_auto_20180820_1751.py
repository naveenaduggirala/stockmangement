# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wine_products', '0002_categorie_label_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='code',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
