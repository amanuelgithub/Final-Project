from django.core.exceptions import ValidationError
from TrafficReport.api.serializes import ReportSerializer
from TrafficReport.models import Report
from rest_framework import generics, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from RecordReport.api.serializers import VehicleSerializer,RecordSerializer
from RecordReport.models import Vehicle,Records

# List Available records .
class ListRecordAPiView(generics.ListAPIView):
    queryset=Records.objects.all()
    serializer_class=RecordSerializer

class RecordList(APIView):
    """ List All Available records """
    def get(self,request):
        records=Records.objects.all()
        serializer=RecordSerializer(records,many=True)

        return Response(serializer.data)





# List User Detail View 
class ListDetailRecordAPiView(generics.RetrieveAPIView):
    queryset=Records.objects.all()
    serializer_class=RecordSerializer



    
class ReportCreateAPiView(generics.CreateAPIView):
    queryset=Report.objects.all()
    serializer_class=ReportSerializer

    def perform_create(self, serializer):
        vehicle_pk=self.kwargs.get("vehicle_pk")
        vehicle=generics.get_object_or_404(Vehicle,pk=vehicle_pk)
        reported_by=self.request.user
        report_queryset=Report.objects.filter(vehicle=vehicle,traffic_police=reported_by)
        if report_queryset.exists():
            raise ValidationError("You have already reported")

        serializer.save(vehicle=vehicle,traffic_police=reported_by)
