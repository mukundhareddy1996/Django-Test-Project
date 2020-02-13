from django import forms

class login(forms.Form):
    username = forms.CharField()
    password = forms.CharField()