from django.contrib import admin
from .models import Plant, CareEvent
from .utils import fetch_gbif_data

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('accession_number', 'scientific_name', 'common_name', 'location')
    search_fields = ('scientific_name', 'common_name', 'accession_number')
    actions = ['update_taxonomy_from_gbif']

    @admin.action(description='Update taxonomy from GBIF')
    def update_taxonomy_from_gbif(self, request, queryset):
        updated_count = 0
        for plant in queryset:
            data = fetch_gbif_data(plant.scientific_name)
            if data:
                # Update scientific name to canonical name if available
                if data.get('canonical_name'):
                     plant.scientific_name = data['canonical_name']
                elif data.get('scientific_name'):
                     plant.scientific_name = data['scientific_name']

                # Update common name if available and empty on plant
                if data.get('common_name') and not plant.common_name:
                    plant.common_name = data['common_name']

                plant.save()
                updated_count += 1

        self.message_user(request, f"Updated taxonomy for {updated_count} plants.")

@admin.register(CareEvent)
class CareEventAdmin(admin.ModelAdmin):
    list_display = ('plant', 'event_type', 'date')
    list_filter = ('event_type', 'date')
