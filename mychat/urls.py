from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("chat/", include("chat.urls")),
    path('auth/', include('chat.urls_auth')), 
    path("admin/", admin.site.urls),
]