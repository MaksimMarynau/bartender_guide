import factory

from account.models import CustomUser, AccountType


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser
    username = factory.Sequence(lambda n: f'user_{n}')
    password = factory.PostGenerationMethodCall('set_password', 'pass')


class AccountTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AccountType
    title = factory.Sequence(lambda n: f'Title_{n}')
