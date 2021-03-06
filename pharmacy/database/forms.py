from .models import Medicines, Category
from django.forms import ModelForm, TextInput, NumberInput, Select
from django import forms

class MedicinesFilterForm(forms.Form):
    category = Category.objects.all()
    
    sort_choices =(
        ("id", "---------"),
        ("price", "Цена"),
        ("name", "Название"),
        ("-popularity", "Популярность"),
        ("count", "Количество"),
    )

    select = forms.ModelChoiceField(label='', required=False, queryset=category, widget=forms.Select(attrs={'class': 'form-select'}))
    sort = forms.ChoiceField(label='', choices=sort_choices, required=False, widget=forms.Select(attrs={'class': 'form-select'}))

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
                'placeholder': 'Цена товара',
            }),
            'count': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество товара',
            })
        }
