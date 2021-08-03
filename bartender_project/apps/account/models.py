from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _


class AccountManager(UserManager):
    def create_user(self, email, username, password=None):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    email = models.EmailField(
        verbose_name=_('email'),
        max_length=60,
        unique=True,
        blank=True,
    )
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name=_('date joined'),
        auto_now_add=True,
    )
    last_login = models.DateTimeField(
        verbose_name=_('last login'),
        auto_now=True,
    )
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    account_type = models.ForeignKey(
        'AccountType',
        verbose_name=_('Account type'),
        null=True,
        on_delete=models.SET_NULL)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class AccountType(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=20,
        unique=True
    )
    make_cocktail = models.BooleanField(
        verbose_name=_('Make cocktail'),
        default=False,
        help_text=_('If True, bartender can add own cocktail')
    )
    add_ingredient = models.BooleanField(
        verbose_name=_('Add ingredient'),
        default=False,
        help_text=_('If True, bartender can add ingredients')
    )
    generate_temp_link = models.BooleanField(
        verbose_name=_('Generate temporary link'),
        default=False,
        help_text=_(
            'If True, bartender will have option to generate temporary link')
    )

    def __str__(self):
        return self.title
