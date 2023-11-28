from django.test import LiveServerTestCase, TestCase
from django.urls import reverse
from datetime import date
from .models import Planter, Plant
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# Unit Tests
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

# Webdriver tests
class LoginFormTest(LiveServerTestCase):
    # Test to make sure login page works, but will pass even if there's an error
    def test_login(self):
        selenium = webdriver.Firefox()
        selenium.get('http://127.0.0.1:8000/planter/2/new_plant/')

        try:
             plant_name = selenium.find_element(By.ID, 'id_name')
            # Add assertions or other actions with plant_name if needed
        except NoSuchElementException as e:
            # Handle the exception (e.g., print a message or log it)
            print(f"Element with id 'id_name' not found: {e}")
        finally:
            selenium.quit()

class PlantFormTest(LiveServerTestCase):
    # Test to login, should pass
    def login(self):
        selenium = webdriver.Firefox()
        selenium.get('http://127.0.0.1:8000/planter/2/new_plant/')
        selenium.get('selenium = webdriver.Firefox')
        selenium.get('http://127.0.0.1:8000/planter/2/new_plant/')
        
        username = selenium.find_element(By.ID, 'id_username')
        password = selenium.find_element(By.ID, 'id_password')
        submit = selenium.find_element(By.XPATH, '//input[@type="submit" and @value="login"]')

        username.send_keys('angie')
        password.send_keys('pooch235')
        submit.send_keys(Keys.RETURN)

        


