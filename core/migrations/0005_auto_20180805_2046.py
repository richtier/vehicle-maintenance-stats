# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-05 20:17
from __future__ import unicode_literals

from datetime import datetime
from django.db import migrations

import csv


fixtures = [
    'csv_fixtures/audi.csv',
    'csv_fixtures/maestrovan.csv',
    'csv_fixtures/peugeot205.csv',
    'csv_fixtures/peugeot.csv',
    'csv_fixtures/skoda.csv',
]

def format_date(raw_string):
    if raw_string:
        return datetime.strptime(raw_string, '%d/%m/%Y %H:%M:%S')
    return None


def create_vehicles(apps, schema_editor):
    Vehicle = apps.get_model("core", "Vehicle")
    Fuel = apps.get_model("core", "Fuel")

    for fixture in fixtures:
        with open(fixture, 'r' ) as f:
            reader = csv.DictReader(f)
            for line in reader:
                vehicle = Vehicle.objects.get(name=line['Vehicle'])
                Fuel.objects.create(
                    date=format_date(line['Date']),
                    miles=line['Miles'] or None,
                    litres=line['Litres'] or None,
                    price_per_litre=line['Price Ltr'] or None,
                    vehicle=vehicle,
                )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180805_2050'),
    ]

    operations = [
        migrations.RunPython(create_vehicles)
    ]
