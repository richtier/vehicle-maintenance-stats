import pygal

from core import models


class MilesPerGallonChart:

    def __init__(self, vehicle_id):
        self.vehicle = models.Vehicle.objects.get(pk=vehicle_id)
        self.chart = pygal.Line(x_label_rotation=90, x_labels_major_every=10)
        self.chart.title = self.vehicle.name + ' Miles per gallon'

    def render(self):       
        data = self.vehicle.fuel_set.all().order_by('date').values('date', 'miles', 'litres')
        self.chart.x_labels = [item['date'].strftime('%Y-%m-%d') for item in data]

        miles = [item['miles'] for item in data]
        gallons = [item['litres']/4.54609 for item in data]
        miles_per_gallon = [(x - miles[i - 1])/gallons[i] for i, x in enumerate(miles)][1:]

        self.chart.add(self.vehicle.name, miles_per_gallon, show_dots=False)
        self.chart.add('Moving average', moving_average(miles_per_gallon), show_dots=False)
        return self.chart.render(is_unicode=True)


def moving_average(values):
    N = 3
    cumsum = [0]
    moving_averages = []
    for i, x in enumerate(values, 1):
        cumsum.append(cumsum[i-1] + x)
        if i>=N:
            moving_ave = (cumsum[i] - cumsum[i-N])/N
            moving_averages.append(moving_ave)
    return moving_averages
