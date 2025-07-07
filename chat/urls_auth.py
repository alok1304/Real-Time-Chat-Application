from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views_auth import signup_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', LoginView.as_view(template_name='chat/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
