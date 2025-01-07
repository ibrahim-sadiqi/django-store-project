from django import forms
from contact_module.models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['title', 'full_name', 'email', 'message']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'subject'
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'text',
                'id': 'message'
            })
        }

        labels = {
            'full_name': 'Fullname',
            'email': 'Email',
            'title': 'subject',
            'message': 'text'
        }

        error_messages = {
            'full_name': {
                'required': 'Please enter the name and family name',
                'max_length': 'The fullname cannot be more than 50 characters'
            },
            'email': {
                'required': 'Please enter your email',
            },
            'title': {
                'required': 'Please enter the subject',
            },
            'message': {
                'required': 'Please enter the text',
            },
        }
