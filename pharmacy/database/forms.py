from .models import Medicines
from django.forms import ModelForm, TextInput, NumberInput, Select
from django import forms
from .models import Category


class MedicinesFilterForm(forms.Form):
    category = Category.objects.all()
    CHOICE = [('Все', 'Все')]

    for u in category:
        CHOICE.append((u.name, u.name))

    CHOICE = tuple(CHOICE)
    select = forms.ChoiceField(label='',choices=CHOICE)


class MedicinesForm(ModelForm):
    class Meta:
        model = Medicines
        fields = ['category', 'name', 'price', 'count']

        widgets = {
            'category': Select(attrs={
                'class': 'form-select',
                'placeholder': 'Категория',
                'name': 'category',
                'id': 'id_category',
                'required': '',
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена товара'
            }),
            'count': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество товара'
            })
        }
