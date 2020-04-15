from django import forms
from models.models import City

class CityForm(forms.Form):
    name = forms.CharField(max_length=25)
