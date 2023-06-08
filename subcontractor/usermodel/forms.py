from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class CustomUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'class':'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password', 'class':'form-control'})

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'company_name', 'proprietor_name', 'phone_number', 'address')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'