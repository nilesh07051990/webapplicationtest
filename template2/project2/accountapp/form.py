from django import forms
from .models import CreateAccount

class CreateAccountForm(forms.ModelForm):
    class Meta:
        model=CreateAccount
        fields= '__all__'