from django.db import models

class Client(models.Model):
    name = models.CharField('ФИО', max_length=300)
    address = models.CharField('Адрес', max_length=255)
    age = models.IntegerField('Возраст')
    phone = models.CharField('Телефон', max_length=12)
    email = models.EmailField('E-mail')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'