from django.db import models
from django.contrib.auth.models import  AbstractUser


class User(AbstractUser):
    avator = models.ImageField(upload_to='images/profile/',  verbose_name='Picture', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='Active Code')
    about_user = models.TextField(verbose_name='About', null=True, blank=True)
    address = models.CharField(max_length=400, null=True, blank=True, verbose_name='Address')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.username

