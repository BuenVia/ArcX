from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # Clients - CRUD
    path('clients/', views.clients_page, name='clients'),
    path('clients/new', views.client_new, name='client_new'),
    path('clients/<id>', views.client_edit, name='client_edit'),
    path('client_docs/<id>', views.client_document_view, name='client_docs'),
    path('clients/password/<id>', views.client_pw_edit, name='client_pw_edit'),
    # Documents - CRUD
    path('documents/', views.document_view, name='admin_documents'),
    path('delete_pdf/<int:pdf_id>/', views.delete_pdf, name='admin_delete_pdf'),
    # Equipment - CRUD
    path('equipment/<int:id>/', views.admin_equipment, name='admin_equipment'),
    # Competency - CRUD
    path('competency/<int:id>/', views.admin_competency, name='admin_competency'),
]
