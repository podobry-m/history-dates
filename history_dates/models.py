from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime

class HistoricalEvent(models.Model):
    title = models.TextField(verbose_name="Событие")
    date = models.PositiveSmallIntegerField(verbose_name="Дата (год)", validators=[MaxValueValidator(datetime.now().year,'Ошибка, год не может быть больше текущего')])
    def __str__(self):
        return f"{self.date} - {self.title}"

    class Meta:
        ordering = ['date']
        verbose_name = "Историческое событие"
        verbose_name_plural = "Исторические события"
