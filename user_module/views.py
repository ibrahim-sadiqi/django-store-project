from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from utils.email_service import send_email
from .models import User
from django.http import  Http404, HttpRequest
from user_module.forms import UserRegistrationForm, UserLoginForm, ForgetPasswordForm, ResetPasswordForm
from django.utils.crypto import get_random_string


class UserRegistrationView(View):
    def get(self, request):
        register_form = UserRegistrationForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'user_module/register.html', context)

    def post(self, request):
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_passwd = register_form.cleaned_data.get('passwd')
            print("user passwd", user_passwd)
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'The email has already existed in system')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False,
                    username=user_email)
                new_user.set_password(user_passwd)
                new_user.save()
                # send email active account
                send_email(subject='Account Activation', to=new_user.email,
                           context={'user': new_user},
                           template_name='emails/activate_account.html')
                return redirect(reverse('login_page'))
        context = {
            'register_form': register_form
        }
        return render(request, 'user_module/register.html', context)


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect(reverse('login_page'))
            else:
                # todo shows the massege for user that show your acount has already activated
                pass
        raise Http404


class UserLoginView(View):
    def get(self, request):
        login_form = UserLoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'user_module/login.html', context)

    def post(self, request: HttpRequest):
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user_passwd = login_form.cleaned_data.get('passwd')
            user_email = login_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            print('user', user)
            if user is not None:
                if user.is_active:
                    if user.check_password(user_passwd):
                        login(request, user)
                        print('Logined')
                        return redirect(reverse('index_page'))
                    else:
                        login_form.add_error('email', 'something is wrong')
                else:
                    print('is not activated')
                    login_form.add_error('email', 'Your account has not been activated')
            else:
                login_form.add_error('email', 'something is wrong')
        context = {
            'login_form': login_form
        }
        return render(request, 'user_module/login.html', context)


class ForgetPasswordView(View):
    def get(self, request):
        forget_passwd_form = ForgetPasswordForm()
        context = {
            'forget_passwd_form': forget_passwd_form
        }
        return render(request, 'user_module/forget_password.html', context)

    def post(self, request: HttpRequest):
        forget_passwd_form = ForgetPasswordForm(request.POST)
        if forget_passwd_form.is_valid():
            user_email = forget_passwd_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email(subject='Reset Password', to=user_email,
                           context={'user': user},
                           template_name='emails/forget_password.html')
                return redirect(reverse('login_page'))
        context = {
            'forget_passwd_form': forget_passwd_form
        }
        return render(request, 'user_module/forget_password.html', context)


class ResetPasswordView(View):
    def get(self, request, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login_page'))

        reset_passwd_form = ResetPasswordForm()
        context = {
            'reset_passwd_form': reset_passwd_form,
            'user': user
        }
        return render(request, 'user_module/reset_password.html', context)

    def post(self, request: HttpRequest, active_code):
        reset_passwd_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_passwd_form.is_valid():
            if user is None:
                return redirect(reverse('login_page'))
            else:
                new_passwd = reset_passwd_form.cleaned_data.get('passwd')
                user.set_password(new_passwd)
                user.email_active_code = get_random_string(72)
                user.is_active = True
                user.save()
                return redirect(reverse('login_page'))

        context = {
            'reset_passwd_form': reset_passwd_form,
            'user': user
        }
        return render(request, 'user_module/reset_password.html', context)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login_page'))





