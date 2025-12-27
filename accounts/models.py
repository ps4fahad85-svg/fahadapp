from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    """
    بيانات إضافية لأي مستخدم (مستفيد / مستشار / مشرف)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)
    is_consultant = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Profile - {self.user.username}"


class Specialty(models.Model):
    """
    تخصصات الاستشارات (نفسية، اجتماعية، أسرية...)
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ConsultantProfile(models.Model):
    """
    بيانات المستشار التفصيلية
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialties = models.ManyToManyField(Specialty, related_name="consultants")
    bio = models.TextField()
    price_per_session = models.DecimalField(max_digits=8, decimal_places=2)
    years_of_experience = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Consultant - {self.user.username}"
