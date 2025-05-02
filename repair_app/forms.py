from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Device, RepairOrder


class UserRegistrationForm(UserCreationForm):
    """Форма для реєстрації користувачів"""
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class DeviceForm(forms.ModelForm):
    """Форма для створення та редагування пристроїв"""

    class Meta:
        model = Device
        fields = ['name', 'model', 'serial_number', 'purchase_date', 'description']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
        }


class RepairOrderForm(forms.ModelForm):
    """Форма для створення замовлення ремонту"""

    class Meta:
        model = RepairOrder
        fields = ['device', 'service', 'issue_description']

    def __init__(self, user=None, *args, **kwargs):
        super(RepairOrderForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['device'].queryset = Device.objects.filter(user=user)
