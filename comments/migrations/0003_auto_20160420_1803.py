# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 18:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20160420_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='company_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='companies.Company'),
        ),
    ]