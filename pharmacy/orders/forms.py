from .models import Orders, StatusOrder
from database.models import Medicines
from client.models import Client
from django.forms import ModelForm, CheckboxInput, DateInput, Select
from django import forms


class OrdersFilterForm(forms.Form):
    statusOrder = StatusOrder.objects.all()
    status = forms.ModelChoiceField(
        label='', required=False, queryset=statusOrder, widget=forms.Select(attrs={'class': 'form-select'}))

class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['medicines', 'client', 'extradition_date']

        widgets = {
            'medicines': Select(attrs={
                'class': 'form-select',
                'placeholder': 'Медикамент',
            }),
            'client': Select(attrs={
                'class': 'form-select',
                'placeholder': 'Клиент',
            }),
            'extradition_date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата выдачи',
            }),
        }
