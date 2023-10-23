from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('schair_data_api/', views.schair_data_api, name='schair_data_api'),
    path('', views.schair_data_view, name='schair_data_view'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='schair_app/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='schair_app/logout.html'),name='logout'),

]
