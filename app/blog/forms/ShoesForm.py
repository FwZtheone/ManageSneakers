from django import forms

class ShoesForm(forms.Form):
    name = forms.CharField(label="Name",max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    size = forms.FloatField(label="Size",widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.FloatField(label="Price",widget=forms.TextInput(attrs={'class':'form-control'}))
    color = forms.CharField(label="Color",widget=forms.TextInput(attrs={'class':'form-control'}))
    price_bought = forms.FloatField(label="Price bought",widget=forms.TextInput(attrs={'class':'form-control'}))
    price_selled = forms.FloatField(label="Price selled",widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    date_received = forms.DateTimeField(label="Date received",widget=forms.TextInput(attrs={'class':'form-control'}))
    date_selled = forms.DateTimeField(label="Date selled",widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    quantity = forms.IntegerField(label="Quantity",widget=forms.TextInput(attrs={'class':'form-control'}))
    damaged = forms.BooleanField(label="Damaged",widget=forms.TextInput(attrs={'class':'form-check-input',"type":"checkbox"}),required=False)
    selled = forms.BooleanField(label="Selled",widget=forms.TextInput(attrs={'class':'form-check-input',"type":"checkbox"}),required=False)