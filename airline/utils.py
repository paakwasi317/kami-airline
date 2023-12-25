import math
from typing import List, Union, TypedDict

Value = Union[int, float]

Item = TypedDict('Item', {
  'key': str,
  'value': Value  
})

class Airplane:

    @staticmethod
    def _calculate_fuel_tank_capacity(airplane_id: int) -> int:
        return 200 * airplane_id
    
    @staticmethod
    def _calculate_base_fuel_consumption(airplane_id: int) -> float:
        return math.log(airplane_id) * 0.80

    def calculate_fuel_consumption(self, airplane_id: int, num_passengers: int) -> float:
        return self._calculate_base_fuel_consumption(airplane_id) + num_passengers * 0.002
    
    def calculate_max_fly_minutes(self, airplane_id: int, num_passengers: int) -> float:
        fuel_consumption_per_minute = self.calculate_fuel_consumption(airplane_id, num_passengers)
        max_fly_minutes = self._calculate_fuel_tank_capacity(airplane_id) / fuel_consumption_per_minute
        return math.ceil(max_fly_minutes)
    
    def calculator(self, airplane_inputs: list) -> List[Item]:
        calculated_results = []
        airplanes = airplane_inputs['airplanes']
        for airplane in airplanes: 
            airplane_id = airplane['airplane_id']
            number_of_passengers = airplane['number_of_passengers']
            fuel_consumption = self.calculate_fuel_consumption(airplane_id, number_of_passengers)
            max_fly_minutes = self.calculate_max_fly_minutes(airplane_id, number_of_passengers)
            data = dict(max_fly_minutes=max_fly_minutes, fuel_consumption=fuel_consumption, airplane_id=airplane_id, number_of_passengers=number_of_passengers)
            calculated_results.append(data)
        return calculated_results