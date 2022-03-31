
from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="name",max_length=100,)
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="last name", max_length=100)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}),label="email", max_length=255)
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="password", max_length=255)