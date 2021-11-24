from django import forms
from django.contrib.auth.models import User
from . import models
class UserForm(forms.ModelForm):
   password = forms.CharField(widget=forms.PasswordInput)
   class Meta:

      model = models.User
      fields = ('username', 'password')
class UserInfoForm(forms.ModelForm):
    class Meta:
        model=models.Members
        exclude=['username','last_played']
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=500, label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")
   # password = forms.CharField(widget=forms.PasswordInput)
   # class Meta:
   #   model=User
   #
   #   fields=('username','password')



