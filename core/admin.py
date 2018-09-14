import datetime

from django.contrib import admin
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls import url
from django.urls import reverse

from core import charts, models


admin.site.site_header = 'Vehicle Stats'


class MilesPerGallonView(TemplateView):
    template_name = 'core/miles-per-gallon.html'

    def get_context_data(self, **kwargs):
        chart = charts.MilesPerGallonChart(vehicle_id=self.kwargs['pk'])
        return super(MilesPerGallonView, self).get_context_data(
            chart=chart.render(),
            opts=models.Vehicle._meta,
            has_view_permission=True,
            original='Miles per gallon',
            **kwargs
        )


@admin.register(models.Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    search_fields = ('name', 'registration',)
    list_display = (
        'name',
        'registration',
        'year_manufactured',
        'miles_per_gallon_button'
    )


    def miles_per_gallon_button(self, obj):
        return '<a href="{url}">View miles per gallon</a>'.format(
            url=reverse("admin:miles-per-gallon", kwargs={'pk': obj.pk})
        )

    def get_urls(self):
        return [
            url(
                r'^(?P<pk>[0-9]+)/miles-per-gallon/$',
                self.admin_site.admin_view(
                    MilesPerGallonView.as_view()
                ),
                name="miles-per-gallon"
            ),
        ] + super(VehicleAdmin, self).get_urls()

    miles_per_gallon_button.short_description = ''
    miles_per_gallon_button.allow_tags = True


@admin.register(models.Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'date',)
    list_filter = ('vehicle', )


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ( 'date', 'vehicle', 'type_of_service', 'miles',)
    list_filter = (
        'vehicle',
        'type_of_service',
        'oil',
        'diesel_filter',
        'air_filter',
    )
