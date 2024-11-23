from django import forms

class StudentForm(forms.Form):
    name=forms.CharField()
    marks=forms.IntegerField()
    def clean_name(self):
        print('validating name field')
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError('The minimum number of characters should be 4')
        return inputname
