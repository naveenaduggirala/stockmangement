# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wine_products', '0001_initial'),
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
                ('categorie', models.ForeignKey(to='wine_products.Categorie')),
                ('products', models.ForeignKey(to='wine_products.Product')),
                ('qunatity', models.ForeignKey(to='wine_products.Qunatite')),
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
                ('stoct_of_products', models.IntegerField()),
                ('categorie', models.ForeignKey(to='wine_products.Categorie')),
                ('products', models.ForeignKey(to='wine_products.Product')),
                ('qunatity', models.ForeignKey(to='wine_products.Qunatite')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
