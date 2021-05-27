from django.db import models

class Category(models.Model):
    name = models.CharField('Наименование категории', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Medicines(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    name = models.CharField('Название', max_length=255)
    price = models.FloatField('Цена')
    count = models.IntegerField('Кол-во')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Медикамент'
        verbose_name_plural = 'Медикаменты'
