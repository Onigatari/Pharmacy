from django.db import models
from datetime import date
from database.models import Medicines, Category
from client.models import Client

class StatusOrder(models.Model):
    status = models.CharField(max_length=256)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'

#default=StatusOrder.objects.get(status="Активен")
class Orders(models.Model):
    medicines = models.ForeignKey(Medicines, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    received = models.ForeignKey(StatusOrder, on_delete=models.PROTECT, default=StatusOrder.objects.get(status="Активен"))
    registration_date = models.DateField('Время регистрации', default=date.today)
    extradition_date = models.DateField('Время выдачи')

    def __str__(self):
        return self.client.surname + " " + self.client.name + " " +  self.client.patronymic + " | " + self.medicines.name + " | " + self.registration_date.strftime('%d-%m-%Y')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'