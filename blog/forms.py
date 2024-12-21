from django import forms
from django.forms import ModelForm
from .models import Student, school, hotel, shop

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields= '__all__'

class schoolForm(forms.ModelForm):
    class Meta:
        model=school
        fields= '__all__'

class shopForm(forms.ModelForm):
    class Meta:
        model=shop
        fields= '__all__'


class hotelForm(forms.ModelForm):
    class Meta:
        model=hotel
        fields='__all__'
