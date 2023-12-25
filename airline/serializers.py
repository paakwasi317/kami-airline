from rest_framework import serializers

class AirplaneInputSerializer(serializers.Serializer):
    number_of_passengers = serializers.IntegerField(required=True)
    airplane_id = serializers.IntegerField(required=True)

    def validate(self, data):

        if not (data['airplane_id'] and data['number_of_passengers']):
            raise serializers.ValidationError("airplane_id and number of passengers can not be empty/zero")
        

        return data


class AirplaneListInputSerializer(serializers.ListSerializer):
    child = AirplaneInputSerializer()


class AirplaneBulkInputSerializer(serializers.Serializer):
    airplanes = AirplaneListInputSerializer()

    def validate(self, data):
        airplanes_data = data.get('airplanes', [])

        if not airplanes_data:
            raise serializers.ValidationError("Airplanes list can not be empty")
        
        if len(airplanes_data) > 10:
            raise serializers.ValidationError("List must contain a maximum of 10 items")
        
        return data
    

class AirplaneOutputSerializer(AirplaneInputSerializer):
    fuel_consumption = serializers.FloatField()
    max_fly_minutes = serializers.IntegerField()
    