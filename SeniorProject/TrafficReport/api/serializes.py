from django.db.models import fields
from rest_framework import serializers
from TrafficReport.models import MobileDevices, Report,TrafficPolice
from RecordReport.models import Records




class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Records
        fields="__all__"




class ReportSerializer(serializers.ModelSerializer):

    # reports=serializers.StringRelatedField(many=True)




    class Meta:
        model=Report
        fields=['description','records','traffic_police','created_at']





    def create(self,validated_data):
        reports_record=RecordSerializer.create(RecordSerializer(),validated_data)
        reports,created=Records.objects.create(records=reports_record)
        return reports


class MobileDeviceSerializer(serializers.ModelSerializer):
    """Serializer For MobileDevice Identification"""
    class Meta:
        model=MobileDevices
        fields=('participants','token')


    def create(self,validated_data):
        """ Creating MobileDeice instances """
        return MobileDevices.objects.create(**validated_data)

