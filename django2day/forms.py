from django import forms
from django.forms import ModelForm
from .models import Beginning
class InputForm(forms.Form):

    first_name=forms.CharField(max_length=200)
    last_name=forms.CharField(max_length=200)
    roll_number=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput())

class InputForm(forms.Form):

    first_name=forms.CharField(max_length=200)
    last_name=forms.CharField(max_length=200)
    age=forms.IntegerField()
    email=forms.EmailInput()
    gender=forms.CharField()

class BeginningForm(ModelForm):
    class Meta:
        model=Beginning
        fields="__all__"


