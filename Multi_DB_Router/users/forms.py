"""Forms for users."""
from .models import CustomUser
from django import forms
# from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.ModelForm):
    """Established Business for Sale form."""

    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

    class Meta:
        """Definition for this class."""

        model = CustomUser
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        """Override fields objects."""
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = True
        self.fields['email'].required = True

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': self.fields[field].label
            })


class SignUpForm(forms.ModelForm):
    """Customer Form."""

    class Meta:
        """Meta Info."""

        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'database']

    def __init__(self, *args, **kwargs):
        """Override fields objects."""
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['password'].required = True
        self.fields['email'].required = True

        for field in iter(self.fields):
            if field != 'database':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': self.fields[field].label
                })
