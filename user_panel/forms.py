from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from user_module.models import User


class EditUserPanelModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avator', 'address', 'about_user']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'subject'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full name'
            }),
            'avator': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'address',

            }),

            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'address',

            }),

           'about_user': forms.Textarea(attrs={
                'class': 'form-control',
            })
        }

        labels = {
            'first_name': 'Name',
            'last_name': 'Last Name',
            'avator': 'Picture',
            'address': 'Address',
            'about_user': 'About'

        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='Current Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter current password'}),

    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'}),
        validators=[
            validators.MinLengthValidator(8)
        ]
    )
    conf_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm the new password'}),
        validators=[
            validators.MinLengthValidator(8)
        ]
    )

    def clean(self):
        cleaned_data = super().clean()
        passwd = cleaned_data.get('password')
        conf_passwd = cleaned_data.get('conf_password')
        if passwd != conf_passwd:
            raise ValidationError('Passwords do not match')
        return cleaned_data
