# coding=utf-8
from django.contrib.auth.models import User
from django.db import models

class Selfie(models.Model):
    user = models.ForeignKey(User, editable = False)
    selfie_before = models.ImageField(verbose_name="Фотография до")
    selfie_after = models.ImageField(verbose_name="Фотография после")

    balls = models.IntegerField(default=0, verbose_name="Оценка")
    is_rated = models.BooleanField(default=False, verbose_name="Есть ли оценка")

    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    date_rated = models.DateTimeField(auto_now_add=True, verbose_name="Дата оценки")