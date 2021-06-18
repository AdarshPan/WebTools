from django import forms
from .models import *


class ImageForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = ['Image']
        labels={'Image':""}