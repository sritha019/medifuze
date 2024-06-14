from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, home, redirect_dashboard, doctor_dashboard, patient_dashboard, book_test, book_appointment, download_report, agent_dashboard

urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', redirect_dashboard, name='dashboard'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
    path('agent_dashboard/', agent_dashboard, name='agent_dashboard'),
    path('book_test/', book_test, name='book_test'),
    path('book_appointment/', book_appointment, name='book_appointment'),
    path('download_report/', download_report, name='download_report'),
]
