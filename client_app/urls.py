from django.urls import path
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from .forms import CustomPasswordChangeForm
from . import views

urlpatterns = [
    path('', views.client_login, name='client_login'),
    path('logout/', views.client_logout, name='client_logout'),  # Assuming you have a logout view
    path('dashboard/', views.client_dashboard, name='client_dashboard'),
    # Documentation
    path('documents/upload/<int:id>/', views.upload_document, name='upload_document'),
    path('documents/', views.document_review, name="document_review"),
    # Staff
    path('staff/', views.client_staff, name='client_staff'),
    # Equipment
    
    # Password
    path('password_change/', PasswordChangeView.as_view(
        form_class=CustomPasswordChangeForm,
        template_name='client_app/password_change.html',
        success_url=reverse_lazy('password_change_done')
    ), name='password_change'),
        path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='client_app/password_change_done.html'
    ), name='password_change_done'),
]

