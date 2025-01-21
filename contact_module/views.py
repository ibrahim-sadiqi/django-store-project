from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView

from site_module.models import SiteSetting
from .forms import ContactUsModelForm
from .models import UserProfile


class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context


class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = ['image']
    success_url = '/contact-us/create-profile'


class ListProfileView(ListView):
    model = UserProfile
    template_name = 'contact_module/list_profile_page.html'
    context_object_name = 'profiles'


