from .models import Orders, StatusOrder
from database.models import Medicines, Category
from client.models import Client
from django.forms import ModelForm, CheckboxInput, DateInput, Select
from django import forms


class OrdersFilterForm(forms.Form):
    statusOrder = StatusOrder.objects.all()
    category = Category.objects.all()
    medicines = Medicines.objects.all()
    
    status = forms.ModelChoiceField(
        label='', required=False, queryset=statusOrder, widget=forms.Select(attrs={'class': 'form-select'}))
    find_category =forms.ModelChoiceField(
        label='', required=False, queryset=category, widget=forms.Select(attrs={'class': 'form-select'}))
    find_medicines =forms.ModelChoiceField(
        label='', required=False, queryset=medicines, widget=forms.Select(attrs={'class': 'form-select'}))

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
                'type': 'date', 
                'id': 'example-date-input',
            }),
        }
