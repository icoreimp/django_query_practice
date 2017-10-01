# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-01 06:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Principle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('contact_no', models.CharField(max_length=256)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=45)),
                ('weight', models.CharField(max_length=45)),
                ('mop', models.CharField(max_length=45)),
                ('pouch', models.IntegerField(blank=True, null=True)),
                ('current_price_activated_on', models.DateField(blank=True, null=True)),
                ('distributor_price', models.FloatField(blank=True, null=True)),
                ('sell_price', models.FloatField(default=0.0)),
                ('vat_manufacturer', models.FloatField(blank=True, null=True)),
                ('vat_distributor', models.FloatField(blank=True, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('status', models.BooleanField(default=True)),
                ('principal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Principle')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductCategory'),
        ),
    ]
