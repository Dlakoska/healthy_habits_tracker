from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Модель пользователя
    """
    username = models.CharField(max_length=30, unique=True, verbose_name="Никнейм")
    email = models.EmailField(unique=True, verbose_name="Email")
    telegram_id = models.CharField(max_length=200, verbose_name="телеграм айди", null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
