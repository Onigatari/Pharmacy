from .models import Medicines
from django.forms import ModelForm, TextInput, NumberInput

class MedicinesForm(ModelForm):
    class Meta:
        model = Medicines
        fields = ['name', 'prise', 'count']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'prise': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена товара'
            }),
            'count': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество товара'
            }),
        }