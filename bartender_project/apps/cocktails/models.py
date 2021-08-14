from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import CustomUser
from ingredients.models import Ingredient


class Style(models.Model):
    title_s = models.CharField(verbose_name=_('Title'),max_length=30,)

    class Meta:
        verbose_name='Style'
        verbose_name_plural='Styles'
        ordering = ('title_s',)

    def __str__(self):
        return self.title_s


class Cocktail(models.Model):
    name = models.CharField(verbose_name=_('Name of cocktail'), max_length=40)
    slug = models.SlugField(verbose_name=_('Slug'),
                            db_index=False)
    serve_in = models.CharField(verbose_name=_('Serve in'),max_length=30)
    garnish = models.CharField(verbose_name=_('Garnish'),max_length=30)
    how_to_make = models.TextField(verbose_name=_('How to make'),)
    cocktail_ingredients = models.ManyToManyField(
        'CocktailIngredient',related_name='cocktails_list')
    review = models.CharField(verbose_name=_('Review'),max_length=100)
    history = models.TextField(verbose_name=_('History'),)
    nutrition = models.CharField(verbose_name=_('Nutrition'),max_length=50)
    bartender = models.ForeignKey(CustomUser,on_delete=models.CASCADE,)
    style = models.ManyToManyField('Style', related_name='cocktails')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(verbose_name=_('Draft'),default=False)

    class Meta:
        verbose_name='cocktail'
        verbose_name_plural='Cocktails'
        ordering = ('name',)
        unique_together = (('slug','name'),)

    def __str__(self):
        return self.name

class CocktailIngredient(models.Model):
    how_many = models.PositiveSmallIntegerField(blank=False)
    ingredients = models.ForeignKey(Ingredient,
                                    on_delete=models.RESTRICT,
                                    related_name='cocktail_ingredients')

    class Meta:
        verbose_name='Cocktail ingredient'
        verbose_name_plural='Cocktail ingredients'

    def __str__(self):
        return f'{self.ingredients.title_i} {self.how_many} ml'
