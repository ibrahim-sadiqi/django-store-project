from django.db import models


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Name')
    site_url = models.URLField(max_length=200, null=True, blank=True, verbose_name='Url')
    about_us_text = models.TextField(null=True, blank=True, verbose_name='About Us')
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='Address')
    phone = models.CharField(max_length=14, blank=True, null=True, verbose_name='Phone')
    email = models.EmailField(max_length=200, blank=True, null=True, verbose_name='Email')
    fax = models.CharField(max_length=200, blank=True, null=True, verbose_name='Fax')
    copy_right = models.CharField(max_length=400, blank=True, null=True, verbose_name='Copy Right Text')
    site_logo = models.ImageField(upload_to='images/site-settings/', verbose_name='Logo')
    is_main_setting = models.BooleanField(verbose_name='Main Setting')

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')

    class Meta:
        verbose_name = 'Footer Link Category'
        verbose_name_plural = 'Footer Links Categories'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    url = models.URLField(max_length=500, verbose_name='link')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='Category')

    class Meta:
        verbose_name = 'Footer Link'
        verbose_name_plural = 'Footer Links'

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    url = models.URLField(max_length=500, verbose_name='Url')
    url_title = models.CharField(max_length=200, verbose_name='Url title')
    disc = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='images/sliders/', verbose_name='Picture')
    is_active = models.BooleanField(default=True, verbose_name='Active/deactive')

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

    def __str__(self):
        return self.title