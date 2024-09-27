from django.urls import path
from . import views

urlpatterns = [
    path("", views.AccountView.as_view()),
    path("login/", views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
]