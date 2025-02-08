from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='title')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='title on url ')
    is_active = models.BooleanField(default=True, verbose_name='Enable/Disable')
    is_delete = models.BooleanField(default=False, verbose_name='Deleted/ Not deleted')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, verbose_name='Brand name', db_index=True)
    url_title = models.CharField(max_length=200, verbose_name='Url Name', db_index=True)
    is_active = models.BooleanField(verbose_name='Active / Deactive')

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300)
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='categories')
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='picture')
    brand = models.ForeignKey(ProductBrand, verbose_name='Brand', on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(verbose_name='Price')
    short_desc = models.CharField(max_length=400, db_index=True, verbose_name='Short Description')
    main_desc = models.TextField(verbose_name='Main Description', db_index=True)
    is_active = models.BooleanField(verbose_name='active / deactive')
    slug = models.SlugField(default="", null=False, blank=True, editable=False, unique=True)
    is_delete = models.BooleanField(verbose_name='Deleted / Not')

    def get_absolute_url(self):
        return reverse(viewname='product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}, {self.price}, {self.short_desc}, {self.is_active}"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='tag')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')
    is_active = models.BooleanField(verbose_name='active / deactive')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'Product Tag'
        verbose_name_plural = 'Product Tags'
