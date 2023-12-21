from django import forms

class practiceForm(forms.Form):
    name = forms.CharField(label="Enter your name")
    email = forms.EmailField(label="Enter your Email")