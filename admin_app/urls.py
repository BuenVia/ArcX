from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='aa_login'),
    path('logout/', views.admin_logout, name='aa_logout'),
    path('dashboard/', views.aa_dashboard, name='aa_dashboard'),
    # Clients - CRUD
    path('clients/', views.aa_clients_list, name='aa_clients'),
    path('clients/create', views.aa_client_create, name='aa_client_create'),
    path('clients/read/<int:id>', views.aa_client_read, name='aa_client_read'),
    path('clients/update/<int:id>', views.aa_client_update, name='aa_client_update'),
    path('clients/delete/<int:id>', views.aa_client_delete, name='aa_client_delete'),
    path('clients/password/<int:id>', views.aa_client_update_pw, name='aa_client_pw_edit'),
    # Documents - CRUD
    path('documents/', views.document_view, name='admin_documents'),
    path('delete_pdf/<int:pdf_id>/', views.delete_pdf, name='admin_delete_pdf'),
    # Equipment - CRUD
    path('equipment/', views.admin_all_equipment, name='admin_all_equipment'),
    path('equipment/all/', views.admin_all_equipment_new, name='admin_all_equipment_new'),
    path('equipment/all/<int:id>', views.admin_all_equipment_edit, name='admin_all_equipment_edit'),
    path('equipment/all/delete/<int:id>', views.admin_all_equipment_delete, name='admin_all_equipment_delete'),
    path('equipment/<int:id>/', views.admin_client_equipment, name='admin_equipment'),
    # Competency - CRUD
    path('competency/<int:id>/', views.admin_competency, name='admin_competency'),
    path('competency/staff/<int:id>/', views.admin_competency_staff, name='admin_competency_staff'),
    path('competency/staff/add/<int:user_id>', views.add_or_edit_staff, name='admin_competency_staff_add'),
    path('competency/staff/edit/<int:user_id>/<int:staff_id>/', views.add_or_edit_staff, name='admin_competency_staff_edit'),
]
