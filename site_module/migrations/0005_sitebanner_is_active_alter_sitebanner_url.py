# Generated by Django 5.1.3 on 2025-02-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0004_sitebanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitebanner',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Enable/Disable'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sitebanner',
            name='url',
            field=models.URLField(blank=True, max_length=400, null=True, verbose_name='Banner URL'),
        ),
    ]
