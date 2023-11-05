from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from app.models import Registration


class ContactForm(forms.Form):
    Name = forms.CharField(max_length=50)
    Email = forms.EmailField()
    Subject = forms.CharField(max_length=100)
    Message = forms.CharField(widget=forms.Textarea)

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ( '__all__')

        widgets = {
            'First_Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Last_Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Gender' :forms.TextInput(attrs={'class':'form-control'}),
            'Date_of_Birth' :forms.DateInput(attrs={'class':'form-control'}),
            'Email' :forms.EmailInput(attrs={'class':'form-control'}),
            'Mobile' :forms.NumberInput(attrs={'class':'form-control'}),
            'Country' :forms.TextInput(attrs={'class':'form-control'}),
            'State' :forms.TextInput(attrs={'class':'form-control'}),
            'City' :forms.TextInput(attrs={'class':'form-control'}),
            'Hobbies' :forms.TextInput(attrs={'class':'form-control'}),
        }


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))
    new_password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))
    new_password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')