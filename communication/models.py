from django.db import models
from django.contrib.auth import get_user_model
from consultations.models import Session

User = get_user_model()


class Conversation(models.Model):
    """
    محادثة مرتبطة بجلسة
    """
    session = models.OneToOneField(
        Session, on_delete=models.CASCADE, related_name="conversation"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation - Session #{self.session.id}"


class Message(models.Model):
    """
    رسائل داخل المحادثة
    """
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name="messages"
    )
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender}"


class Notification(models.Model):
    """
    إشعارات النظام
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification - {self.user}"


class Review(models.Model):
    """
    تقييم المستشار بعد الجلسة
    """
    session = models.OneToOneField(Session, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review - Session #{self.session.id}"
