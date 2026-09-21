from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("statistics/", views.statistics, name="statistics"),
    path("applications/add/", views.add_application, name="add_application"),
    path("applications/<int:pk>/", views.application_detail, name="application_detail"),
    path("applications/<int:pk>/edit/", views.edit_application, name="edit_application"),
    path("applications/<int:pk>/delete/", views.delete_application, name="delete_application"),
    path("account/", views.account_settings, name="account_settings"),
path("account/delete/", views.delete_account, name="delete_account"),
]