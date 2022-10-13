from django import forms
from django.forms import ModelForm

from .models import User


class UserForm(ModelForm):
    required_css_class = 'required-field'
    Name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",
                                                         "placeholder": " Прізвище та ім'я"}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control",
                                                            "placeholder": " your_email@ukr.net"}))
    Message = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    def clean_Name(self):
        name_and_surname = self.cleaned_data['Name'].split()
        if len(name_and_surname) != 2:
            raise forms.ValidationError('Неправильно вказане ім\'я та прізвище')
        if not (all(letter.isalpha() for letter in name_and_surname[0])) or not (
                all(letter.isalpha() for letter in name_and_surname[1])):
            raise forms.ValidationError('Неправильно вказане ім\'я та прізвище')
        return self.cleaned_data['Name']

    class Meta:
        model = User
        fields = '__all__'
