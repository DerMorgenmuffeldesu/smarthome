from django.urls import path
from .views import SensorListView, SensorDetailView, MeasurementListView, MeasurementDetailView

urlpatterns = [
    path('sensors/', SensorListView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementListView.as_view()),
    path('measurements/<pk>/', MeasurementDetailView.as_view()),
]