from django import forms
from .models import CustomUser

class ExampleForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise forms.ValidationError("Name must contain only letters.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email:
            raise forms.ValidationError("Enter a valid email address.")
        return email
