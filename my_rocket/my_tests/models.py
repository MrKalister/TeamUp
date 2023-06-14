from django.core.validators import (MaxValueValidator, MinLengthValidator,
                                    MinValueValidator)
from django.db import models


class UniqueLogin(models.Model):
    unique_string = models.CharField(
        max_length=10,
        unique=True,
        null=True,
        blank=True
    )


class IQTestResult(models.Model):
    login = models.OneToOneField(
        UniqueLogin,
        on_delete=models.CASCADE,
        related_name='iq_test',
    )
    points = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)])
    timestamp = models.DateTimeField(auto_now_add=True)


class EQTestResult(models.Model):
    login = models.OneToOneField(
        UniqueLogin,
        on_delete=models.CASCADE,
        related_name='eq_test',
    )
    letters = models.JSONField(
        max_length=5,
        validators=[MinLengthValidator(5)]
    )
    timestamp = models.DateTimeField(auto_now_add=True)
