from django.db import models

class Client(models.Model):
    surname = models.CharField('Фамилия', max_length=300)
    name = models.CharField('Имя', max_length=300)
    patronymic = models.CharField('Отчество', max_length=300)
    address = models.CharField('Адрес', max_length=255)
    date_of_birth = models.DateField('Дата рождения')
    phone = models.CharField('Телефон', max_length=10)
    email = models.EmailField('E-mail')

    def __str__(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'