from django import forms
from django.forms.widgets import NumberInput
import datetime

choice = ['2000', '2001', '2002']
choice2 = ['jan', 'feb', 'mar', 'apr']
color_choices = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('red', 'Red')
]
class practiceForm(forms.Form):
    name = forms.CharField(label="Enter your name")
    comment = forms.CharField(widget=forms.Textarea)
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField(label="Enter your Email")
    agree = forms.BooleanField()
    date = forms.DateField()
    date2 = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    date3 = forms.DateField(widget=forms.SelectDateWidget(years=choice))
    name2 = forms.CharField(initial="My name is ")
    length = forms.CharField(max_length=10)
    agree2 = forms.BooleanField(initial=True)
    day = forms.DateField(initial=datetime.date.today)
    color = forms.ChoiceField(choices=color_choices)
    radio_color = forms.ChoiceField(widget=forms.RadioSelect, choices=color_choices)
    checkbox_color = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=color_choices)