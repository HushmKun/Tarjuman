from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html", redirect_authenticated_user=True), name='login'),
]
