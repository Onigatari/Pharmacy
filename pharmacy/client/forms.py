from django.forms.widgets import DateInput
from .models import Client
from django.forms import ModelForm, TextInput, NumberInput

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['surname', 'name', 'patronymic', 'address', 'date_of_birth', 'phone', 'email']

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
            'date_of_birth': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения',
                'type': 'date', 
                'id': 'example-date-input',
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
