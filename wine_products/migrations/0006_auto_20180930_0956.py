# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wine_products', '0005_qunatite_label_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='label_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='qunatite',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
