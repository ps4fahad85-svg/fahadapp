from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # لوحة التحكم
    path("admin/", admin.site.urls),

    # التطبيقات الأساسية
    path("accounts/", include("accounts.urls")),
    path("consultations/", include("consultations.urls")),
    path("communication/", include("communication.urls")),
]
