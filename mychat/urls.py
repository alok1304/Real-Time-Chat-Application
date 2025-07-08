from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/chat/", permanent=False)),  # 👈 Redirect root to /chat/
    path("chat/", include("chat.urls")),
    path("auth/", include("chat.urls_auth")),
    path("admin/", admin.site.urls),
]
