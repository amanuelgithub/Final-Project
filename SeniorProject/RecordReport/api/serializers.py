from rest_framework import serializers
from RecordReport.models import Vehicle,Records




class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model=Vehicle
        fields=['vehicle_plate','vehicle_type']


class RecordSerializer(serializers.ModelSerializer):
    vehicle=VehicleSerializer(read_only=True)

    class Meta:
        model=Records
        fields=['vehicle','location','vehicle_speed','duration']
