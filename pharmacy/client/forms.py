from .models import Client
from django.forms import ModelForm, TextInput, NumberInput

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['surname', 'name', 'patronymic', 'address', 'age', 'phone', 'email']

        widgets = {
            'surname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'patronymic': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            'address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес',
            }),
            'age': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'
            })
        }
