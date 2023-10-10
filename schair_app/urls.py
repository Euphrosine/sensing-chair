from django.urls import path
from . import views

urlpatterns = [
    path('schair_data_api/', views.schair_data_api, name='schair_data_api'),
    path('schair_data_view/', views.schair_data_view, name='schair_data_view'),
]
