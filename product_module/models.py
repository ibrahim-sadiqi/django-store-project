from django.db import models
from django.core.validators import  MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    short_desc = models.CharField(max_length=400, null=True)
    is_active = models.BooleanField(null=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, editable=False)

    def get_absolute_url(self):
        return reverse(viewname='product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}, {self.price}, {self.rating}, {self.short_desc}, {self.is_active}"
