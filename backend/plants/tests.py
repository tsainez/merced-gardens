from django.test import TestCase, Client
from .models import Plant
import datetime
import os

class PlantTestCase(TestCase):
    def setUp(self):
        self.plant = Plant.objects.create(
            accession_number='TEST-001',
            scientific_name='Aloe vera',
            acquisition_date=datetime.date.today(),
            location='Test Loc'
        )

    def test_qr_code_generated(self):
        """Test that a QR code is generated on save."""
        self.assertTrue(self.plant.qr_code)
        # Ensure the file actually exists
        self.assertTrue(os.path.exists(self.plant.qr_code.path))

    def test_detail_view(self):
        """Test the plant detail view."""
        client = Client()
        response = client.get(f'/plants/{self.plant.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Aloe vera')
        self.assertContains(response, 'TEST-001')
