from django import forms

class AutoForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)