from django.urls import path
from .views import SchairDataAPI, schair_data_view

urlpatterns = [
    path('api/schair_data/', SchairDataAPI.as_view(), name='schair_data_api'),
    path('schair_data/', schair_data_view, name='schair_data_view'),
]
