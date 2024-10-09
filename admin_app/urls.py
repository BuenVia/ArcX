from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('clients/', views.clients_page, name='clients'),
    path('clients/new', views.client_new, name='client_new'),
    path('clients/<id>', views.client_edit, name='client_edit'),
    path('clients/password/<id>', views.client_pw_edit, name='client_pw_edit'),
    path('documents/', views.document_view, name='admin_documents'),
    path('delete_pdf/<int:pdf_id>/', views.delete_pdf, name='admin_delete_pdf'),
]
