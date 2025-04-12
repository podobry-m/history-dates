from django.db import models

class HistoricalEvent(models.Model):
    title = models.TextField(blank=True, verbose_name="Событие")
    date = models.IntegerField(verbose_name="Дата (год)")
    def __str__(self):
        return f"{self.date} - {self.title}"

    class Meta:
        ordering = ['date']
        verbose_name = "Историческое событие"
        verbose_name_plural = "Исторические события"
