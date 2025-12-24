from django.urls import path
from .views import NearestServiceAPI, PageApp

urlpatterns = [
    path('api/nearest-service/', NearestServiceAPI.as_view(), name='nearest-service'),
    path('index/', PageApp, name='App'),
]
