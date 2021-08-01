from django import forms
from django.db  import models
from django.forms import fields
from .models import Student

class StudentRegistrationForms(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"