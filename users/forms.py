from django import forms

class OrderForm(forms.Form):
    qty = forms.IntegerField(min_value=1)
    fullname = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=20)
    address = forms.CharField(max_length=200)

class OrderConfirmForm(forms.Form):
    deliverDate = forms.DateTimeField(input_formats=['%d/%m/%Y %I:%M %p'])