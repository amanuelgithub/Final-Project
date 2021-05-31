from rest_framework import generics
from RecordReport.api.serializers import VehicleSerializer,RecordSerializer
from RecordReport.models import Vehicle,Records


class ListRecordAPiView(generics.ListAPIView):
    queryset=Records.objects.all()
    serializer_class=RecordSerializer



