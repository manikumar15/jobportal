from django import forms
from .models import Search,Register,login,applyjob

class Searchform(forms.ModelForm):
    class Meta:
        model=Search
        fields = "__all__"

class regform(forms.ModelForm):
    class Meta:
        model=Register
        fields = "__all__"

class logregform(forms.ModelForm):
    class Meta:
        model=login
        fields = "__all__"

class loginform(forms.Form):
      username = forms.CharField(required=False)
      password = forms.CharField(max_length=20) 

class applyform(forms.ModelForm):
    class Meta:
        model=applyjob
        fields = "__all__"