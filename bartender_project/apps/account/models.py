# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
#
#
# class CustomUser(AbstractUser):
#     account_type = models.ForeignKey(
#         'AccountType',
#         verbose_name=_('Account type'),
#         null=True,
#         on_delete=models.SET_NULL)
#
#     def __str__(self):
#         return self.username
#
#
# class AccountType(models.Model):
#     title = models.CharField(
#         verbose_name=_('Title'),
#         max_length=20,
#         unique=True
#     )
#     make_cocktail = models.BooleanField(
#         verbose_name=_('Make cocktail'),
#         default=False,
#         help_text=_('If True, bartender can add own cocktail')
#     )
#     add_ingredient = models.BooleanField(
#         verbose_name=_('Add ingredient'),
#         default=False,
#         help_text=_('If True, bartender can add ingredients')
#     )
#     generate_temp_link = models.BooleanField(
#         verbose_name=_('Generate temporary link'),
#         default=False,
#         help_text=_(
#             'If True, bartender will have option to generate temporary link')
#     )
#
#     def __str__(self):
#         return self.title
