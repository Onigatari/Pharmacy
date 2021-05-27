from .models import Orders
from database.models import Medicines
from client.models import Client
from django.forms import ModelForm, CheckboxInput, DateInput, Select 

class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['medicines', 'client', 'registration_date', 'extradition_date', 'received']

        widgets = {
            'medicines': Select(attrs={
                'class': 'form-select',
                'placeholder': 'Медикамент',
                'name': 'medicines',
                'id': 'id_medicines',
                'required': '',
            }),
            'client': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Клиент',
                'name': 'client',
                'id': 'id_client',
                'required': '',
            }),
            'extradition_date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата выдачи'
            }),
            'received': CheckboxInput(attrs={
                'class': 'form-control',
                'placeholder': 'Получин'
            })
        }
