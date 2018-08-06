# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-05 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='year_manufactured',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='year_purchased',
            field=models.DateField(blank=True, null=True),
        ),
    ]
