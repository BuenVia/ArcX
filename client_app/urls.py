from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_login, name='client_login'),
    path('dashboard/', views.client_dashboard, name='client_dashboard'),
    path('logout/', views.client_logout, name='client_logout'),  # Assuming you have a logout view
]
