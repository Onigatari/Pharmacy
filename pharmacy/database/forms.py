from typing import List
from django.db.models.enums import Choices, ChoicesMeta
from django.db.models.fields.related import ForeignKey
from django.forms.widgets import CheckboxInput, SelectMultiple
from .models import Medicines
from django.forms import ModelForm, TextInput, NumberInput, Select 


class MedicinesForm(ModelForm):
    class Meta:
        model = Medicines
        fields = ['category', 'name', 'prise', 'count']

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
            'prise': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена товара'
            }),
            'count': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество товара'
            })
        }
