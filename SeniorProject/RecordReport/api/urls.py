from django.urls import path
from RecordReport.api.views import ListRecordAPiView,ListDetailRecordAPiView,ReportCreateAPiView

urlpatterns = [
    path('records/',ListRecordAPiView.as_view(),name='list-rcords'),
    path('records/<int:pk>',ListDetailRecordAPiView.as_view(),name='list-detail'),
    path('records/<int:pk>/report',ReportCreateAPiView.as_view(),name='create-record')
    
]