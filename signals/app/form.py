from .models import *
from django import forms

class Mymodelform(forms.ModelForm):
    class Meta:
        model = Mymodel
        filds = ['name','description']