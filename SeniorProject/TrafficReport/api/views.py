from rest_framework import serializers
from TrafficReport.models import Records,Report
from TrafficReport.api.serializes import ReportSerializer,RecordSerializer
from rest_framework import generics
from rest_framework import mixins


class ReportCreateApiView(generics.CreateAPIView):
    queryset=Report.objects.all()
    serializer_class=ReportSerializer

    
