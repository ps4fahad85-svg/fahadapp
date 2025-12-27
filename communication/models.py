from django.db import models
from django.contrib.auth import get_user_model
from consultations.models import Session

User = get_user_model()


class Conversation(models.Model):
    """
    محادثة مرتبطة بجلسة
    """

    session = models.OneToOneField(
        Session,
        on_delete=models.CASCADE,
        related_name="conversation",
        verbose_name="الجلسة",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء",
    )

    class Meta:
        verbose_name = "محادثة"
        verbose_name_plural = "المحادثات"

    def __str__(self):
        return f"محادثة - جلسة رقم {self.session.id}"


class Message(models.Model):
    """
    رسائل داخل المحادثة
    """

    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages",
        verbose_name="المحادثة",
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_messages",
        verbose_name="المرسل",
    )
    content = models.TextField(
        verbose_name="محتوى الرسالة",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإرسال",
    )

    class Meta:
        verbose_name = "رسالة"
        verbose_name_plural = "الرسائل"
        ordering = ("-created_at",)

    def __str__(self):
        return f"رسالة من {self.sender}"


class Notification(models.Model):
    """
    إشعارات النظام
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications",
        verbose_name="المستخدم",
    )
    title = models.CharField(
        max_length=200,
        verbose_name="العنوان",
    )
    body = models.TextField(
        verbose_name="المحتوى",
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name="مقروء",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء",
    )

    class Meta:
        verbose_name = "إشعار"
        verbose_name_plural = "الإشعارات"
        ordering = ("-created_at",)

    def __str__(self):
        return f"إشعار - {self.user}"


class Review(models.Model):
    """
    تقييم المستشار بعد الجلسة
    """

    session = models.OneToOneField(
        Session,
        on_delete=models.CASCADE,
        related_name="review",
        verbose_name="الجلسة",
    )
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="المستفيد",
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name="التقييم",
        help_text="قيمة من 1 إلى 5",
    )
    comment = models.TextField(
        blank=True,
        verbose_name="تعليق",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء",
    )

    class Meta:
        verbose_name = "تقييم"
        verbose_name_plural = "التقييمات"
        ordering = ("-created_at",)

    def __str__(self):
        return f"تقييم - جلسة رقم {self.session.id}"
