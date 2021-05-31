from django.urls import path
from RecordReport.api.views import ListRecordAPiView

urlpatterns = [
    path('records/',ListRecordAPiView.as_view(),name='list-rcords')
    
]