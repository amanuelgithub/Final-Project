from django.conf import settings
from django.db.models import fields
from rest_auth.models import TokenModel
from rest_auth.utils import import_callable
from rest_auth.serializers import UserDetailsSerializer as DefaultUserDetailsSerializer


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

rest_auth_serializers=getattr(settings,'REST_AUTH_SERIALIZERS',{})
DefaultUserDetailsSerializer=import_callable(
    rest_auth_serializers.get('USER_DETAILS_SERIALIZER',DefaultUserDetailsSerializer)
)

class CustomTokenSerializer(serializers.ModelSerializer):
    user=DefaultUserDetailsSerializer(read_only=True)
    class Meta:
        model=TokenModel
        fields=('key','user',)
