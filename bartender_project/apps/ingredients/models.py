from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import CustomUser


class Category(models.Model):
    title_c = models.CharField(
        verbose_name=_('Title of category'),
        max_length=20,
        unique=True,)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('title_c',)

    def __str__(self):
        return self.title_c


class Ingredient(models.Model):
    title_i = models.CharField(verbose_name=_('Title of ingredient'),
                               max_length=50,
                               blank=False,
                               default='')
    slug = models.SlugField(verbose_name=_('Slug'),
                            db_index=False)
    alc_product_of = models.PositiveSmallIntegerField(
        verbose_name=_('Alc product of'),)
    aroma = models.CharField(verbose_name=_('Aroma'),
                             max_length=100,
                             blank=False,
                             default='')
    taste = models.CharField(verbose_name=_('Taste'),
                             max_length=200,
                             blank=False,
                             default='')
    description = models.TextField(verbose_name=_('Description'),
                                   blank=False,
                                   default='')
    size = models.PositiveSmallIntegerField(verbose_name=_('Size (ml)'),)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(verbose_name=_('Draft'), default=False)
    category = models.ManyToManyField('Category', related_name='ingredients')
    bartender = models.ForeignKey(
        CustomUser,
        null=True,
        on_delete=models.SET_NULL,
        related_name='bartender_ingredients')

    def __str__(self):
        return self.title_i
