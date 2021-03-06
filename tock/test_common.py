import datetime
import unittest

from django.test import TestCase, override_settings
from django.contrib.auth.models import User, Group

from employees.models import UserData


@override_settings(
    PASSWORD_HASHERS=['django.contrib.auth.hashers.MD5PasswordHasher'],
    AUTHENTICATION_BACKENDS=[
        'django.contrib.auth.backends.ModelBackend',
        'uaa_client.authentication.UaaBackend',
    ],
)
class BaseLoginTestCase(TestCase):

    def create_user(self, username, password=None, is_staff=False,
                    is_superuser=False, email=None, groups=(),
                    start_date=datetime.datetime(2014, 1, 1),
                    end_date=datetime.datetime(2016, 1, 1)):

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )

        try:
            UserData.objects.get(user=user)
        except UserData.DoesNotExist:
            UserData(
                user=user,
                start_date=start_date,
                end_date=end_date
            ).save()

        for groupname in groups:
            group = Group.objects.get(name=groupname)
            group.user_set.add(user)
            group.save()

        if is_staff:
            user.is_staff = True
            user.save()

        if is_superuser:
            user.is_staff = True
            user.is_superuser = True
            user.save()

        return user

    def login(self, username='first.last', is_staff=False, is_superuser=False,
              groups=(), permissions=None,
              start_date=datetime.datetime(2014, 1, 1),
              end_date=datetime.datetime(2016, 1, 1)):

        user = self.create_user(username=username, password='example',  # nosec
                                is_staff=is_staff, is_superuser=is_superuser,
                                groups=groups,
                                start_date=start_date,
                                end_date=end_date)

        assert self.client.login(  # nosec
            username=username,
            password='example'  # nosec
        )
        return user


class ProtectedViewTestCase(BaseLoginTestCase):

    url = None

    def assertRedirectsToLogin(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response['Location'],
            '/auth/login/?next=%s' % url
        )

    def test_login_is_required(self):
        if not self.url:
            raise unittest.SkipTest()
        self.assertRedirectsToLogin(self.url)
