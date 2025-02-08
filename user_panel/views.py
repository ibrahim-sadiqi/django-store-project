from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from user_module.models import User
from .forms import EditUserPanelModelForm, ChangePasswordForm


class UserPanelView(TemplateView):
    template_name = 'user_panel/user_panel_page.html'


class EditUserPanelView(View):
    def get(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_user = EditUserPanelModelForm(instance=current_user)
        context = {
            'form': edit_user,
            'current_user': current_user
        }
        return render(request, 'user_panel/edit_user_panel_profile.html', context)

    def post(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_user = EditUserPanelModelForm(request.POST, request.FILES, instance=current_user)
        if edit_user.is_valid() :
            edit_user.save(commit=True)
        context = {
            'form': edit_user,
            'current_user': current_user
        }
        return render(request, 'user_panel/edit_user_panel_profile.html', context)


class ChangePasswordView(View):
    def get(self, request):
        context = {
            'form': ChangePasswordForm()
        }
        return render(request, 'user_panel\change_password_page.html', context)

    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(form.cleaned_data.get('current_password')):
                current_user.set_password(form.cleaned_data.get('password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login_page'))
            else:
                form.add_error('current_password', 'You current password is wrong')
        context = {
            'form': form
        }
        return render(request, 'user_panel\change_password_page.html', context)


def user_panel_components(request):
    return  render(request, 'user_panel/components/user_panel_component_page.html')