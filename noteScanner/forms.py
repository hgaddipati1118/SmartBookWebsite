
# forms.py
from django import forms
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["main_Img","action"]
class fake(forms.ModelForm):
    class Meta:
        model = Image
        fields = []
class fake2(forms.ModelForm):
    class Meta:
        model = Image
        fields = []