# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-10-12 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20221012_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electricmeterreading',
            name='documents',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Document'),
        ),
        migrations.AlterField(
            model_name='fuel',
            name='documents',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Document'),
        ),
        migrations.AlterField(
            model_name='housecontents',
            name='documents',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Document'),
        ),
        migrations.AlterField(
            model_name='service',
            name='documents',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Document'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='documents',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Document'),
        ),
    ]