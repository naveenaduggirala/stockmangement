# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_count_saled_today', models.IntegerField()),
                ('total_price', models.CharField(max_length=100, null=True, blank=True)),
                ('categorie', models.ForeignKey(to='products.Categorie')),
                ('products', models.ForeignKey(to='products.Product')),
                ('qunatity', models.ForeignKey(to='products.Qunatite')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stoct_of_products', models.CharField(max_length=100, null=True, blank=True)),
                ('cl_op_balance', models.CharField(max_length=100, null=True, blank=True)),
                ('categorie', models.ForeignKey(to='products.Categorie')),
                ('products', models.ForeignKey(to='products.Product')),
                ('qunatity', models.ForeignKey(to='products.Qunatite')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
