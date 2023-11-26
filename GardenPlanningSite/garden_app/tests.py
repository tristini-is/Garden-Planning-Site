from django.test import TestCase
from django.urls import reverse
from datetime import date
from .models import Planter, Plant

class PlanterModelTest(TestCase):

    def setUp(self):
        self.planter = Planter.objects.create(name="Test Planter")

    def test_str_method(self):
        self.assertEqual(str(self.planter), "Test Planter")

    def test_get_absolute_url(self):
        expected_url = reverse('planter-detail', args=[str(self.planter.id)])
        self.assertEqual(self.planter.get_absolute_url(), expected_url)


class PlantModelTest(TestCase):

    def setUp(self):
        self.planter = Planter.objects.create(name="Test Planter")
        self.plant = Plant.objects.create(
            name="Test Plant",
            care="Test Care Instructions",
            plantDate=date.today(),
        )

    def test_str_method(self):
        self.assertEqual(str(self.plant), "Plant object (1)")

    def test_get_absolute_url(self):
        expected_url = reverse('plant-detail', args=[str(self.plant.id)])
        self.assertEqual(self.plant.get_absolute_url(), expected_url)

    def test_plant_date_in_past(self):
        self.assertTrue(self.plant.plantDate <= date.today())
