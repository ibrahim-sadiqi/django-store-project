from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_email(subject, to, context, template_name):
    try:
        from_email = settings.EMAIL_HOST_USER
        html_message = render_to_string(template_name, context)
        plain_message = strip_tags(html_message)
        send_mail(subject, plain_message, from_email, [to], html_message=html_message, fail_silently=False)
    except Exception as ex:
        print(ex)
