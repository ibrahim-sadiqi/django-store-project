from django.db import models
from user_module.models import User


class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', null=True, blank=True,
                               on_delete=models.CASCADE,
                               verbose_name='Parent category')
    title = models.CharField(max_length=300, verbose_name='Title of category')
    url_title = models.CharField(max_length=400, unique=True, verbose_name='Title of Url')
    is_active = models.BooleanField(default=True, verbose_name='Enable/Disable')

    class Meta:
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title of Article')
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True, verbose_name='Title of Url')
    image = models.ImageField(upload_to='images/articles/', verbose_name='Picture')
    short_desc = models.TextField(verbose_name='Short Description')
    text = models.TextField(verbose_name='Text of article')
    is_active = models.BooleanField(default=True, verbose_name='Enable/Disable')
    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name='Categories')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', null=True, editable=False)
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Registration Date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Article')
    parent = models.ForeignKey('ArticleComment', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Parent')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Create Date')
    text = models.TextField(verbose_name='Text')

    class Meta:
        verbose_name = 'Article Comment'
        verbose_name_plural = 'Article Comments'

    def __str__(self):
        return str(self.user)
