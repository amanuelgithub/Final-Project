from django.urls import path
from TrafficReport.api.views import ReportCreateApiView,MobileDevicesCreateAPIView,fcm_insert

urlpatterns = [
    path('report',ReportCreateApiView.as_view(),name="create-report"),
    path('insert',fcm_insert,name='insert-token')
]

