from django.urls import path
from TrafficReport.api.views import ReportCreateApiView

urlpatterns = [
    path('report',ReportCreateApiView.as_view(),name="create-report")
]

