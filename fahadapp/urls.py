from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # الرئيسية
    path("", TemplateView.as_view(template_name="home.html"), name="home"),

    # لوحة التحكم
    path("admin/", admin.site.urls),

    # التطبيقات الأساسية
    path("accounts/", include("accounts.urls")),
    path("consultations/", include("consultations.urls")),
    path("communication/", include("communication.urls")),
]

# ✅ عرض ملفات media أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
