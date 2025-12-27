from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    """
    الملف الشخصي للمستخدم
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="المستخدم",
        related_name="profile",
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="رقم الهاتف",
    )
    is_consultant = models.BooleanField(
        default=False,
        verbose_name="هل هو مستشار؟",
    )
    is_verified = models.BooleanField(
        default=False,
        verbose_name="تم التحقق",
    )

    class Meta:
        verbose_name = "الملف الشخصي"
        verbose_name_plural = "الملفات الشخصية"

    def __str__(self):
        return f"الملف الشخصي - {self.user.username}"


class Specialty(models.Model):
    """
    تخصصات الاستشارات (نفسية، اجتماعية، أسرية...)
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="اسم التخصص",
    )

    class Meta:
        verbose_name = "تخصص"
        verbose_name_plural = "التخصصات"

    def __str__(self):
        return self.name


class ConsultantProfile(models.Model):
    """
    بيانات المستشار التفصيلية
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="المستشار",
        related_name="consultant_profile",
    )
    specialties = models.ManyToManyField(
        Specialty,
        related_name="consultants",
        verbose_name="التخصصات",
    )
    bio = models.TextField(
        verbose_name="نبذة تعريفية",
    )
    price_per_session = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="سعر الجلسة",
    )
    years_of_experience = models.PositiveIntegerField(
        default=0,
        verbose_name="سنوات الخبرة",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="نشط",
    )

    class Meta:
        verbose_name = "ملف المستشار"
        verbose_name_plural = "ملفات المستشارين"

    def __str__(self):
        return f"المستشار - {self.user.username}"
