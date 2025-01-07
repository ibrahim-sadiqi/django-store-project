from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, ListView
from .forms import ContactUsModelForm
from .models import UserProfile


class ContactUsView(FormView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def form_valid(self, form):
        form.save()
        return super(ContactUsView, self).form_valid(form)


class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = ['image']
    success_url = '/contact-us/create-profile'


class ListProfileView(ListView):
    model = UserProfile
    template_name = 'contact_module/list_profile_page.html'
    context_object_name = 'profiles'


