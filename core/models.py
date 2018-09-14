from datetime import datetime

from django.db import models


class ElectricMeterReading(models.Model):
    date = models.DateTimeField(primary_key=True)
    meter_reading = models.IntegerField(blank=True, null=True)
    actual_reading_date = models.CharField(max_length=100, blank=True, null=True)
    actual_reading = models.IntegerField(blank=True, null=True)
    estmate_or_reading = models.BooleanField()
    fixed_charge = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    rate_1_per_kwhr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    rate_2_per_kwhr = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    rate_1_break = models.IntegerField(blank=True, null=True)
    other_costs = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)


class HouseContents(models.Model):
    manufacters_name = models.CharField(max_length=100, blank=True, null=True)
    manfacter_model = models.CharField(max_length=100, blank=True, null=True)
    serial_no = models.CharField(max_length=100, blank=True, null=True)
    value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    entered = models.DateTimeField(blank=True, null=True)
    purchased = models.CharField(max_length=100, blank=True, null=True)
    invoice_no = models.CharField(max_length=100, blank=True, null=True)


class Vehicle(models.Model):
    name = models.CharField(max_length=24)
    registration = models.CharField(max_length=16, blank=True, null=True)
    year_manufactured = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    year_purchased = models.DateField(blank=True, null=True)
    vendor = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    class Meta:
        ordering = ['-date']

    vehicle = models.ForeignKey(Vehicle)
    type_of_service = models.CharField(max_length=100, blank=True, null=True)
    materials = models.TextField(blank=True, null=True)
    oil = models.BooleanField()
    diesel_filter = models.BooleanField()
    air_filter = models.BooleanField()
    miles = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)


class Fuel(models.Model):
    class Meta:
        ordering = ['-date']

    date = models.DateField(blank=True, null=True, default=datetime.utcnow)
    miles = models.FloatField(blank=True, null=True)
    litres = models.FloatField(blank=True, null=True)
    price_per_litre = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        blank=True,
        null=True,
        help_text='Price per litre in pounds and pence.'
    )
    vehicle = models.ForeignKey(Vehicle)

    def __str__(self):
        return self.vehicle.name
