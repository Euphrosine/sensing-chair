from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('schair_data_api/', views.schair_data_api, name='schair_data_api'),
    path('', views.schair_data_view, name='schair_data_view'),
    path('dashboard_data/', views.dashboard_data, name='dashboard_data'),
    path('update-data/', views.update_data, name='update_data'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='schair_app/login.html'),name='login'),
    path('dashboard_data/logout/',auth_views.LogoutView.as_view(template_name='schair_app/logout.html'),name='logout'),
    
    # ml urls
    path('predict_posture/', views.predict_posture, name='predict_posture'),
    path('popup/', views.popup, name='popup'),
]
