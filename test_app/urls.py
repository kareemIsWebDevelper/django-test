# from django.contrib.auth.views import LoginView, LogoutView
from .views import homeView
from django.urls import path


urlpatterns = [
    path('', homeView.as_view(), name='home'),
]