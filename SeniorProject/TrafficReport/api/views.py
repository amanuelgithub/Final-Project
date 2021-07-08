from django.http.response import HttpResponse
from rest_framework import serializers
from TrafficReport.models import Records,Report,MobileDevices
from TrafficReport.api.serializes import ReportSerializer,RecordSerializer,MobileDeviceSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated


class ReportCreateApiView(generics.ListCreateAPIView):
    queryset=Report.objects.all()
    serializer_class=ReportSerializer
    permission_classes=[IsAuthenticated,]


class MobileDevicesCreateAPIView(generics.CreateAPIView):
    queryset=MobileDevices.objects.all()
    serializer_class=MobileDeviceSerializer




def fcm_insert(request):
    token=request.GET.get("fcm_token","")
    user_id=request.GET.get("user_id","")

    mobile_device=MobileDevices(participants=user_id,token=token)
    mobile_device.save()

    return HttpResponse(token)
    
    

    
