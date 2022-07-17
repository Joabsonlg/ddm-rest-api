from rest_framework.test import APITestCase

from users.models import User


class AuthTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='a2d4g6j8'
        )
        self.url = '/api/v1/jwt/create/'
        self.user_token = self.login({
            'username': 'testuser',
            'password': 'a2d4g6j8'
        }).data['access']

    def login(self, data):
        return self.client.post(self.url, data, format='json')

    def test_login(self):
        """
        Ensure we can login a user.
        """
        data = {
            'username': 'testuser',
            'password': 'a2d4g6j8'
        }
        response = self.login(data)
        self.assertEqual(response.status_code, 200)

    def test_login_with_wrong_password(self):
        """
        Ensure we can not login a user with wrong password.
        """
        data = {
            'username': 'testuser',
            'password': 'wrong_password'
        }
        response = self.login(data)
        self.assertEqual(response.status_code, 401)

    def test_login_with_wrong_username(self):
        """
        Ensure we can login a user.
        """
        data = {
            'username': 'wrong_username',
            'password': 'a2d4g6j8'
        }
        response = self.login(data)
        self.assertEqual(response.status_code, 401)

    def test_verify_token(self):
        """
        Ensure we can verify a token.
        """
        url = '/api/v1/jwt/verify/'
        data = {
            'token': self.user_token
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)


class UserTestCase(APITestCase):
    def setUp(self):
        self.url = '/api/v1/users/'

    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        url = '/api/v1/users/'
        data = {
            'username': 'testuser',
            'email': 'teste@email.com',
            'password': 'a2d4g6j8',
            're_password': 'a2d4g6j8'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        user = User.objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'teste@email.com')
        self.assertTrue(user.is_active, True)
        self.assertFalse(user.is_staff, False)
        self.assertFalse(user.is_superuser, False)

    def test_create_user_with_commom_password(self):
        """
        Ensure we can create a new user object.
        """
        url = '/api/v1/users/'
        data = {
            'username': 'testuser',
            'email': 'j@g.com',
            'password': '123456',
            're_password': '123456'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_create_user_without_password(self):
        """
        Ensure we can create a new user object.
        """
        url = '/api/v1/users/'
        data = {
            'username': 'testuser',
            'email': 'teste@email.com',
            're_password': 'a2d4g6j8'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['password'], ['Este campo é obrigatório.'])

    def test_create_user_without_username(self):
        """
        Ensure we can create a new user object.
        """
        url = '/api/v1/users/'
        data = {
            'email': 'teste@email.com',
            'password': 'a2d4g6j8',
            're_password': 'a2d4g6j8'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['username'], ['Este campo é obrigatório.'])

    def test_create_user_without_re_password(self):
        """
        Ensure we can create a new user object.
        """
        url = '/api/v1/users/'
        data = {
            'username': 'testuser',
            'email': 'teste@email.com',
            'password': 'a2d4g6j8'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['re_password'], ['Este campo é obrigatório.'])

    def test_create_user_with_wrong_re_password(self):
        """
        Ensure we can create a new user object.
        """
        url = '/api/v1/users/'
        data = {
            'username': 'testuser',
            'email': 'teste@email.com',
            'password': 'a2d4g6j8',
            're_password': 'wrong_password'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)
