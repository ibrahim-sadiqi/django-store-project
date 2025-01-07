from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from django.contrib.auth.password_validation import validate_password


class UserRegistrationForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(),
        validators=[
            validators.EmailValidator()
        ]
    )
    passwd = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        validators=[
            validators.MinLengthValidator(8)
        ]
    )
    conf_passwd = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput()
    )

    # def clean_passwd(self):
    #     passwd = self.cleaned_data.get('passwd')
    #     validate_password(passwd) # django default password validator
    #     return passwd

    def clean(self):
        cleaned_data = super().clean()
        passwd = cleaned_data.get('passwd')
        conf_passwd = cleaned_data.get('conf_passwd')
        if passwd != conf_passwd:
            raise ValidationError('Passwords do not match')
        return cleaned_data


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput()
    )
    passwd = forms.CharField(
        label='Password',
        widget=forms.PasswordInput()
    )


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput()
    )


class ResetPasswordForm(forms.Form):
    passwd = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        validators=[
            validators.MinLengthValidator(8)
        ]
    )
    conf_passwd = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput()
    )

    def clean(self):
        cleaned_data = super().clean()
        passwd = cleaned_data.get('passwd')
        conf_passwd = cleaned_data.get('conf_passwd')
        if passwd != conf_passwd:
            raise ValidationError('Passwords do not match')
        return cleaned_data

