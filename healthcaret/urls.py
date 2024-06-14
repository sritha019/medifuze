from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Ensure logout URL is defined
]
