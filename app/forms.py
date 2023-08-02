from django import forms
from app.models import *

class Employee_Form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
