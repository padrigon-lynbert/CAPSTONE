from django.urls import path
from .views import dashboard_main

app_name = 'Dashboard_main'

urlpatterns = [
    path('dashboard_main/', dashboard_main, name='dashboard_main'),
]
