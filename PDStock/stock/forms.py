from django import forms

class BuscaItemForm(forms.Form):
    item = forms.CharField()