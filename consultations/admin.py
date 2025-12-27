from django.contrib import admin
from .models import Availability, Booking, Session, SessionNote


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("consultant", "day_of_week", "start_time", "end_time")
    list_filter = ("day_of_week",)
    search_fields = ("consultant__username", "consultant__email")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "client",
        "consultant",
        "scheduled_at",
        "status",
        "created_at",
    )
    list_filter = ("status", "scheduled_at")
    search_fields = (
        "client__username",
        "consultant__username",
    )
    date_hierarchy = "scheduled_at"


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        "booking",
        "status",
        "started_at",
        "ended_at",
    )
    list_filter = ("status",)
    search_fields = (
        "booking__client__username",
        "booking__consultant__username",
    )


@admin.register(SessionNote)
class SessionNoteAdmin(admin.ModelAdmin):
    list_display = ("session", "consultant", "created_at")
    search_fields = ("consultant__username",)
    date_hierarchy = "created_at"
