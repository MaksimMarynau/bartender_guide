from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    account_type = models.ForeignKey(
        'AccountType',
        verbose_name=_('Account type'),
        null=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return self.username


class AccountType(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=20,
        unique=True
    )
    make_cocktail = models.BooleanField(
        verbose_name=_('Make cocktail'),
        default=False,
        help_text=_('If True, user can add own cocktail')
    )
    add_ingredient = models.BooleanField(
        verbose_name=_('Add ingredient'),
        default=False,
        help_text=_('If True, user can add ingredients')
    )
    generate_temp_link = models.BooleanField(
        verbose_name=_('Generate temporary link'),
        default=False,
        help_text=_(
            'If True, user will have option to generate temporary link')
    )

    def __str__(self):
        return self.title


class Style(models.Model):
    title_s = models.CharField(verbose_name=_('Title'),max_length=30, unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
    )

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
    ingredients = models.ManyToManyField(
        'IngredientItem',
        through='Ingredient',
        through_fields=("cocktail", "ingredient"),
        related_name='cocktails')
    review = models.CharField(verbose_name=_('Review'),max_length=100)
    history = models.TextField(verbose_name=_('History'),)
    nutrition = models.CharField(verbose_name=_('Nutrition'),max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name='user_cocktails'
    )
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


class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
    )
    text = models.TextField("Message", max_length=5000)
    parent = models.ForeignKey('self',on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"{self.user.username} - {self.cocktail}"

    class Meta:
        verbose_name='Review'
        verbose_name_plural='Reviews'


class Category(models.Model):
    title_c = models.CharField(
        verbose_name=_('Title of category'),
        max_length=20,
        unique=True,)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('title_c',)

    def __str__(self):
        return self.title_c


class Ingredient(models.Model):
    ingredient = models.ForeignKey(
        'IngredientItem',
        on_delete=models.CASCADE,
        related_name='ingredient_item'
    )
    cocktail = models.ForeignKey(
        Cocktail,
        on_delete=models.CASCADE,
        related_name='cocktail_item'
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name=_('Amount'),
        null=True
    )
    dimension = models.CharField(verbose_name=_('Dimension'),max_length=10)


    def __str__(self):
        return f'{self.ingredient.title_i} {self.amount} {self.dimension}'


class IngredientItem(models.Model):
    title_i = models.CharField(
        verbose_name=_('Title of ingredient'),
        max_length=100,
        unique=True,)
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
    category = models.ManyToManyField(Category, related_name='categories')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name='user_ingredients'
    )

    def __str__(self):
        return self.title_i
