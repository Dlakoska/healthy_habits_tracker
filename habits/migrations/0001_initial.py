# Generated by Django 5.1.4 on 2024-12-11 19:49

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        max_length=100,
                        verbose_name="Действие, которое надо сделать",
                    ),
                ),
                (
                    "time",
                    models.TimeField(
                        blank=True,
                        max_length=25,
                        null=True,
                        verbose_name="Время, когда необходимо выполнить привычку",
                    ),
                ),
                (
                    "place",
                    models.CharField(max_length=100, verbose_name="Место"),
                ),
                (
                    "periodicity",
                    models.PositiveSmallIntegerField(
                        default=1,
                        verbose_name="Периодичность выполнения, в днях",
                    ),
                ),
                (
                    "time_to_complete",
                    models.PositiveSmallIntegerField(
                        default=0,
                        verbose_name="Время на выполнение, в секундах",
                    ),
                ),
                (
                    "is_good",
                    models.BooleanField(
                        default=False, verbose_name="Приятная привычка"
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=False, verbose_name="Публичная привычка"
                    ),
                ),
                (
                    "award",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Вознаграждение за выполнение",
                    ),
                ),
                (
                    "created_date",
                    models.DateField(
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="Связанная приятная привычка за выполнение",
                    ),
                ),
            ],
            options={
                "verbose_name": "привычка",
                "verbose_name_plural": "привычки",
                "ordering": ("pk",),
            },
        ),
    ]
