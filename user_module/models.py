from django.db import models
from django.contrib.auth.models import  AbstractUser


class User(AbstractUser):
    avator = models.CharField(max_length=20, verbose_name='Picture', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='Active Code')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.get_full_name()
