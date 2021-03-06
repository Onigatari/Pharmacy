# Generated by Django 3.2 on 2021-06-05 11:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статус',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateField(default=datetime.date.today, verbose_name='Время регистрации')),
                ('extradition_date', models.DateField(verbose_name='Время выдачи')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='client.client')),
                ('medicines', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.medicines')),
                ('received', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.statusorder')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
