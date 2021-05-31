from rest_framework import serializers
from TrafficReport.models import Report,TrafficPolice
from RecordReport.models import Records




class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Records
        fields="__all__"




class ReportSerializer(serializers.ModelSerializer):

    reports=serializers.StringRelatedField(many=True)




    class Meta:
        model=Report
        fields="__all__"





    def create(self,validated_data):
        reports_record=RecordSerializer.create(RecordSerializer(),validated_data)
        reports,created=Records.objects.create(records=reports_record)
        return reports




