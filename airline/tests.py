from django.test import TestCase, Client
import json

from .views import AirplaneListView
from .utils import Airplane

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.airplane = Airplane()
        self.data = {
            "airplanes": [
                {
                    "number_of_passengers": 90,
                    "airplane_id": 8
                }
            ]
        }
        self.expected_value = [
            {
                "number_of_passengers": 90,
                "airplane_id": 8,
                "fuel_consumption": 1.8435532333438687,
                "max_fly_minutes": 868
            }
        ]
        self.more_data = {
            "airplanes": [
                {
                    "number_of_passengers": 90,
                    "airplane_id": 8
                },
                {
                    "number_of_passengers": 90,
                    "airplane_id": 8
                },
                {
                    "number_of_passengers": 90,
                    "airplane_id": 8
                },
                {
                    "number_of_passengers": 90,
                    "airplane_id": 8
                },
                {
                    "number_of_passengers": 90,
                    "airplane_id": 8
                },
                {
                    "number_of_passengers": 90,
                    "airplane_id": 8
                },
                {
                    "number_of_passengers": 90,
                    "airplane_id": 8
                },
                {
                    "number_of_passengers": 90,
                    "airplane_id": 8
                },
                {
                    "number_of_passengers": 90,
                    "airplane_id": 8
                },
                {
                    "number_of_passengers": 90,
                    "airplane_id": 8
                },
                {
                    "number_of_passengers": 90,
                    "airplane_id": 8
                },
                {
                    "number_of_passengers": 90,
                    "airplane_id": 8
                }
            ]
        }

    def test_empty_request(self):
        response = self.client.post('/airplane/calculate', content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_missing_airplanes(self):
        data = {}
        response = self.client.post('/airplane/calculate', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 400)


    def test_with_more_than_10_airplanes(self):
        response = self.client.post('/airplane/calculate', content_type='application/json',data=self.more_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content)['non_field_errors'][0], "List must contain a maximum of 10 items")

    def test_correct_airplane_request(self):
        response = self.client.post('/airplane/calculate', content_type='application/json',data=self.data)
        response = json.loads(response.content)
        self.assertEqual(response, self.expected_value)

    #######################################################
    # Unit Test Airplane calculator                       #
    #######################################################

    def test_fuel_capacity(self):
        capacity = self.airplane.calculate_fuel_consumption(2, 100)
        self.assertEqual(capacity, 0.7545177444479563)

    def test_max_minutes(self):
        minutes = self.airplane.calculate_max_fly_minutes(2, 100)
        self.assertEqual(minutes, 531)

    def test_calculator(self):
        result = self.airplane.calculator(self.data)
        self.assertEqual(result, self.expected_value)