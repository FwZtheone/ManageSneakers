
from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}),label="email", max_length=255)
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="password", max_length=255)