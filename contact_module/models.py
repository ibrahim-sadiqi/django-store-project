from django.db import models


# Create your models here.
class ContactUs(models.Model):
    email = models.EmailField(max_length=300, verbose_name='Email')
    full_name = models.CharField(max_length=300, verbose_name='Full Name')
    title = models.CharField(max_length=300, verbose_name='Title')
    message = models.TextField(verbose_name='Text')
    created_date = models.DateTimeField(verbose_name='Created Date', auto_now_add=True)
    response = models.TextField(verbose_name='Response text with us', null=True, blank=True)
    is_read_by_admin = models.BooleanField(verbose_name='Read by Admin', default=False)

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact us list'

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    image = models.ImageField(upload_to='images/')

