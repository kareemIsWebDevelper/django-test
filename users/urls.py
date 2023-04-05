from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView
from django.urls import path


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='logout'),
]