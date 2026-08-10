from django import forms

class USerForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()