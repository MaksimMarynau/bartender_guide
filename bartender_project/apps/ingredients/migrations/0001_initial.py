# Generated by Django 3.2.5 on 2021-08-14 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_c', models.CharField(max_length=20, verbose_name='Title of category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('title_c',),
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_i', models.CharField(default='', max_length=50, verbose_name='Title of ingredient')),
                ('slug', models.SlugField(db_index=False, verbose_name='Slug')),
                ('alc_product_of', models.PositiveSmallIntegerField(verbose_name='Alc product of')),
                ('aroma', models.CharField(default='', max_length=100, verbose_name='Aroma')),
                ('taste', models.CharField(default='', max_length=200, verbose_name='Taste')),
                ('description', models.TextField(default='', verbose_name='Description')),
                ('size', models.PositiveSmallIntegerField(verbose_name='Size (ml)')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Draft')),
                ('bartender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(related_name='ingredients', to='ingredients.Category')),
            ],
        ),
    ]
