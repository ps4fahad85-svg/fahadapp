from django.contrib import admin
from .models import Profile, Specialty, ConsultantProfile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone_number", "is_consultant", "is_verified")
    list_filter = ("is_consultant", "is_verified")
    search_fields = ("user__username", "user__email", "phone_number")


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(ConsultantProfile)
class ConsultantProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "price_per_session",
        "years_of_experience",
        "is_active",
    )
    list_filter = ("is_active", "specialties")
    search_fields = ("user__username", "user__email")
    filter_horizontal = ("specialties",)
