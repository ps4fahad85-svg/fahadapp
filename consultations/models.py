from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Availability(models.Model):
    """
    أوقات توفر المستشار
    """

    DAYS_OF_WEEK = [
    (0, "الأحد"),
    (1, "الاثنين"),
    (2, "الثلاثاء"),
    (3, "الأربعاء"),
    (4, "الخميس"),
    (5, "الجمعة"),
    (6, "السبت"),
]

    consultant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="availabilities",
        verbose_name="المستشار",
    )
    day_of_week = models.IntegerField(
        choices=DAYS_OF_WEEK,
        verbose_name="يوم الأسبوع",
    )
    start_time = models.TimeField(
        verbose_name="وقت البداية",
    )
    end_time = models.TimeField(
        verbose_name="وقت النهاية",
    )

    class Meta:
        verbose_name = "وقت التوفر"
        verbose_name_plural = "أوقات التوفر"
        ordering = ("day_of_week", "start_time")

    def __str__(self):
        return f"{self.consultant} - {self.get_day_of_week_display()}"


class Booking(models.Model):
    """
    طلب حجز جلسة
    """

    STATUS_CHOICES = [
        ("pending", "قيد الانتظار"),
        ("approved", "مقبول"),
        ("rejected", "مرفوض"),
        ("cancelled", "ملغي"),
    ]

    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings",
        verbose_name="المستفيد",
    )
    consultant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="consultant_bookings",
        verbose_name="المستشار",
    )
    scheduled_at = models.DateTimeField(
        verbose_name="موعد الجلسة",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
        verbose_name="حالة الحجز",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء",
    )

    class Meta:
        verbose_name = "حجز"
        verbose_name_plural = "الحجوزات"
        ordering = ("-created_at",)

    def __str__(self):
        return f"حجز رقم {self.id} - {self.get_status_display()}"


class Session(models.Model):
    """
    الجلسة الفعلية بعد الموافقة
    """

    SESSION_STATUS = [
        ("scheduled", "مجدولة"),
        ("completed", "مكتملة"),
        ("no_show", "لم يحضر"),
        ("cancelled", "ملغاة"),
    ]

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE,
        verbose_name="الحجز",
        related_name="session",
    )
    started_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="وقت البدء",
    )
    ended_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="وقت الانتهاء",
    )
    status = models.CharField(
        max_length=20,
        choices=SESSION_STATUS,
        default="scheduled",
        verbose_name="حالة الجلسة",
    )

    class Meta:
        verbose_name = "جلسة"
        verbose_name_plural = "الجلسات"

    def __str__(self):
        return f"جلسة - حجز رقم {self.booking.id}"


class SessionNote(models.Model):
    """
    ملاحظات الجلسة (خاصة بالمستشار)
    """

    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name="notes",
        verbose_name="الجلسة",
    )
    consultant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="session_notes",
        verbose_name="المستشار",
    )
    note = models.TextField(
        verbose_name="الملاحظة",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء",
    )

    class Meta:
        verbose_name = "ملاحظة جلسة"
        verbose_name_plural = "ملاحظات الجلسات"
        ordering = ("-created_at",)

    def __str__(self):
        return f"ملاحظة - جلسة رقم {self.session.id}"
