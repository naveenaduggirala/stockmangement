# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyMasters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('opening_balance', models.PositiveIntegerField(null=True, blank=True)),
                ('closing_balance', models.PositiveIntegerField(null=True, blank=True)),
                ('categorie', models.ForeignKey(to='products.Categorie')),
                ('products', models.ForeignKey(to='products.Product')),
                ('qunatity', models.ForeignKey(to='products.Qunatite')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DailySales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('count', models.CharField(max_length=100, null=True, blank=True)),
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
                ('stock', models.PositiveIntegerField(null=True, blank=True)),
                ('stock_receive_date', models.DateTimeField(null=True, blank=True)),
                ('categorie', models.ForeignKey(to='products.Categorie')),
                ('products', models.ForeignKey(to='products.Product')),
                ('qunatity', models.ForeignKey(to='products.Qunatite')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
