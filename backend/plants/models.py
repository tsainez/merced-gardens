from django.db import models
from django.conf import settings
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

class Plant(models.Model):
    accession_number = models.CharField(max_length=50, unique=True, help_text="Unique identifier for the plant accessions.")
    scientific_name = models.CharField(max_length=200, help_text="Genus and species.")
    common_name = models.CharField(max_length=200, blank=True, null=True, help_text="Common name if applicable.")
    acquisition_date = models.DateField(help_text="Date when the plant was acquired.")
    source = models.CharField(max_length=200, blank=True, null=True, help_text="Where the plant came from (nursery, donor, etc.).")
    location = models.CharField(max_length=200, help_text="Physical location in the garden or greenhouse.")
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return f"{self.accession_number} - {self.scientific_name}"

    def get_absolute_url(self):
        return f"/plants/{self.id}/"

    def save(self, *args, **kwargs):
        # We save first to ensure we have an ID for the URL
        is_new = self._state.adding
        super().save(*args, **kwargs)

        if is_new or not self.qr_code:
            # Generate QR code
            domain = getattr(settings, 'SITE_URL', 'http://localhost:8000')
            url = f"{domain}{self.get_absolute_url()}"

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            # Save to BytesIO
            buffer = BytesIO()
            img.save(buffer, format='PNG')

            # Save to ImageField
            file_name = f'qr_{self.accession_number}.png'
            self.qr_code.save(file_name, File(buffer), save=False)

            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

            super().save(*args, **kwargs)


class CareEvent(models.Model):
    EVENT_CHOICES = [
        ('water', 'Watering'),
        ('fertilize', 'Fertilizing'),
        ('prune', 'Pruning'),
        ('repot', 'Repotting'),
        ('pest_control', 'Pest Control'),
        ('observation', 'Observation'),
        ('other', 'Other'),
    ]

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='care_events')
    event_type = models.CharField(max_length=50, choices=EVENT_CHOICES)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_event_type_display()} on {self.date} for {self.plant.accession_number}"
