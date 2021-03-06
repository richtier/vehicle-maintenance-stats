# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-05 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricMeterReading',
            fields=[
                ('date', models.DateTimeField(primary_key=True, serialize=False)),
                ('meter_reading', models.IntegerField(blank=True, null=True)),
                ('actual_reading_date', models.CharField(blank=True, max_length=100, null=True)),
                ('actual_reading', models.IntegerField(blank=True, null=True)),
                ('estmate_or_reading', models.BooleanField()),
                ('fixed_charge', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('rate_1_per_kwhr', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('rate_2_per_kwhr', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('rate_1_break', models.IntegerField(blank=True, null=True)),
                ('other_costs', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('miles', models.FloatField(blank=True, null=True)),
                ('litres', models.FloatField(blank=True, null=True)),
                ('price_prl_litre', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HouseContents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacters_name', models.CharField(blank=True, max_length=100, null=True)),
                ('manfacter_model', models.CharField(blank=True, max_length=100, null=True)),
                ('serial_no', models.CharField(blank=True, max_length=100, null=True)),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('entered', models.DateTimeField(blank=True, null=True)),
                ('purchased', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice_no', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_service', models.CharField(blank=True, max_length=100, null=True)),
                ('materials', models.TextField(blank=True, null=True)),
                ('oil', models.BooleanField()),
                ('diesel_filter', models.BooleanField()),
                ('air_filter', models.BooleanField()),
                ('miles', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, serialize=False)),
                ('registration', models.CharField(blank=True, max_length=16, null=True)),
                ('year_manufactured', models.DateTimeField(blank=True, null=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('year_purchased', models.DateTimeField(blank=True, null=True)),
                ('vendor', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Vehicle'),
        ),
        migrations.AddField(
            model_name='fuel',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Vehicle'),
        ),
    ]
