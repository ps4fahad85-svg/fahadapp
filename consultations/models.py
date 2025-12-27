from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Availability(models.Model):
    """
    أوقات توفر المستشار
    """
    consultant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="availabilities"
    )
    day_of_week = models.IntegerField(
        choices=[
            (0, "Monday"),
            (1, "Tuesday"),
            (2, "Wednesday"),
            (3, "Thursday"),
            (4, "Friday"),
            (5, "Saturday"),
            (6, "Sunday"),
        ]
    )
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.consultant} - {self.day_of_week}"


class Booking(models.Model):
    """
    طلب حجز جلسة
    """
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("cancelled", "Cancelled"),
    ]

    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings"
    )
    consultant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="consultant_bookings"
    )
    scheduled_at = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.status}"


class Session(models.Model):
    """
    الجلسة الفعلية بعد الموافقة
    """
    SESSION_STATUS = [
        ("scheduled", "Scheduled"),
        ("completed", "Completed"),
        ("no_show", "No Show"),
        ("cancelled", "Cancelled"),
    ]

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=SESSION_STATUS, default="scheduled"
    )

    def __str__(self):
        return f"Session for Booking #{self.booking.id}"


class SessionNote(models.Model):
    """
    ملاحظات الجلسة (خاصة بالمستشار)
    """
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    consultant = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note - Session #{self.session.id}"
