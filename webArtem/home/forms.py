from django import forms
from .models import Order

class OrderForm(forms.Form):
    name = forms.CharField(label="Ваше имя",max_length=40)
    telephone = forms.CharField(label="Ваш номер телефона")
        # email = forms.EmailField(label="Ваш емейл",
    #                          widget=forms.EmailInput())


class NewOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','telephone']
        widgets = {
        'telephone': forms.NumberInput(attrs={
        'type':'number',
        'placeholder':"Введите Ваш номер телефона",
        }),
        }
