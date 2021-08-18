from django.test import TestCase
from account.factories import AccountTypeFactory

#test models
class AccountTypeTest(TestCase):
    def test__str__(self):
        account_type = AccountTypeFactory()
        self.assertEqual(account_type.title, str(account_type))


#test_permissions


#test_views
