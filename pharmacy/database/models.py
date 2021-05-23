from django.db import models

class Medicines(models.Model):
    name = models.CharField('Название', max_length=255)
    prise = models.FloatField('Цена')
    count = models.FloatField('Кол-во')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Медикамент'
        verbose_name_plural = 'Медикаменты'
