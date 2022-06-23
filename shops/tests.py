from rest_framework.test import APITestCase

from shops.models import Shop, Category
from users.models import User


class CategoryTestCase(APITestCase):

    def setUp(self):
        self.commom_user = User.objects.create_user(
            username='testuser', password='a2d4g6j8', email='test@gmail.com')
        self.admin_user = User.objects.create_user(
            username='adminuser', password='a2d4g6j8', email='admin@gmail.com', is_staff=True, is_superuser=True)
        self.commom_user_token = self.login({
            'username': 'testuser',
            'password': 'a2d4g6j8'
        }).data['access']
        self.admin_user_token = self.login({
            'username': 'adminuser',
            'password': 'a2d4g6j8'
        }).data['access']
        self.base_url = '/api/v1/categories'

    def login(self, data):
        url = '/api/v1/jwt/create/'
        response = self.client.post(url, data, format='json')
        return response

    def create_category(self):
        data = {
            'name': 'Test Category',
            'description': 'This is a test category.'
        }
        return self.client.post(self.base_url, data, format='json',
                                HTTP_AUTHORIZATION='JWT {}'.format(self.admin_user_token))

    def test_create_category(self):
        """
        Ensure we can create a new category object.
        """
        response = self.create_category()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'Test Category')
        self.assertEqual(response.data['description'], 'This is a test category.')

    def test_create_category_without_permission(self):
        """
        Ensure we can't create a category object without permission.
        """
        data = {
            'name': 'Test Category',
            'description': 'This is a test category.'
        }
        response = self.client.post(self.base_url, data, format='json',
                                    HTTP_AUTHORIZATION='JWT {}'.format(self.commom_user_token))
        self.assertEqual(response.status_code, 403)

    def test_list_categories(self):
        """
        Ensure we can list all categories.
        """
        response = self.client.get(self.base_url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_retrieve_category(self):
        """
        Ensure we can retrieve a category object.
        """
        response = self.create_category()
        url = '/api/v1/categories/{}'.format(response.data['slug'])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Category')
        self.assertEqual(response.data['description'], 'This is a test category.')

    def test_update_category(self):
        """
        Ensure we can update a category object.
        """
        response = self.create_category()
        url = '/api/v1/categories/{}'.format(response.data['slug'])
        data = {
            'name': 'Test Category Updated',
            'description': 'This is a test category updated.'
        }
        response = self.client.put(url, data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.admin_user_token))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Category Updated')
        self.assertEqual(response.data['description'], 'This is a test category updated.')

    def test_update_category_without_permission(self):
        """
        Ensure we can't update a category object without permission.
        """
        response = self.create_category()
        url = '/api/v1/categories/{}'.format(response.data['slug'])
        data = {
            'name': 'Test Category Updated',
            'description': 'This is a test category updated.'
        }
        response = self.client.put(url, data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.commom_user_token))
        self.assertEqual(response.status_code, 403)

    def test_delete_category(self):
        """
        Ensure we can delete a category object.
        """
        response = self.create_category()
        url = '/api/v1/categories/{}'.format(response.data['slug'])
        response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.admin_user_token))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Category.objects.count(), 0)

    def test_delete_category_without_permission(self):
        """
        Ensure we can't delete a category object without permission.
        """
        response = self.create_category()
        url = '/api/v1/categories/{}'.format(response.data['slug'])
        response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.commom_user_token))
        self.assertEqual(response.status_code, 403)


class ShopTestCase(APITestCase):
    def setUp(self):
        self.commom_user = User.objects.create_user(
            username='testuser', password='a2d4g6j8', email='test@gmail.com')
        self.admin_user = User.objects.create_user(
            username='adminuser', password='a2d4g6j8', email='admin@gmail.com', is_staff=True, is_superuser=True)
        self.commom_user_token = self.login({
            'username': 'testuser',
            'password': 'a2d4g6j8'
        }).data['access']
        self.admin_user_token = self.login({
            'username': 'adminuser',
            'password': 'a2d4g6j8'
        }).data['access']
        self.base_url = '/api/v1/shops'

    def login(self, data):
        url = '/api/v1/jwt/create/'
        response = self.client.post(url, data, format='json')
        return response

    def create_shop(self):
        sample_user = {
            "name": "Test Shop",
            "username": "Joabson",
            "email": "joabsonlg917@gmail.com",
            "password": "a2d4g6j8",
            "re_password": "a2d4g6j8",
        }
        data = {
            "user": sample_user
        }
        return self.client.post(self.base_url, data, format='json')

    def test_create_shop(self):
        """
        Ensure we can create a new shop object.
        """
        response = self.create_shop()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'Test Shop')
        self.assertEqual(response.data['user'], 3)

    def test_list_shops(self):
        """
        Ensure we can list all shops.
        """
        response = self.client.get(self.base_url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_retrieve_shop(self):
        """
        Ensure we can retrieve a shop object.
        """
        response = self.create_shop()
        url = '/api/v1/shops/{}'.format(response.data['slug'])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Shop')
        self.assertEqual(response.data['user'], 3)

    def test_retrieve_products_shop(self):
        """
        Ensure we can retrieve a shop object.
        """
        response = self.create_shop()
        url = '/api/v1/shops/{}/products'.format(response.data['slug'])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_retrieve_products_shop_with_invalid_slug(self):
        """
        Ensure we can retrieve a shop object.
        """
        url = '/api/v1/shops/invalid/products'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_update_shop(self):
        """
        Ensure we can update a shop object.
        """
        response = self.create_shop()
        url = '/api/v1/shops/{}'.format(response.data['slug'])
        data = {
            'name': 'Test Shop Updated',
            'user': self.commom_user.id
        }
        response = self.client.put(url, data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.commom_user_token))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Shop Updated')
        self.assertEqual(response.data['user'], self.commom_user.id)

    def test_update_shop_without_user(self):
        """
        Ensure we can't update a shop object without user.
        """
        response = self.create_shop()
        url = '/api/v1/shops/{}'.format(response.data['slug'])
        data = {
            'name': 'Test Shop Updated'
        }
        response = self.client.put(url, data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.commom_user_token))
        self.assertEqual(response.status_code, 400)

    def test_update_shop_without_name(self):
        """
        Ensure we can't update a shop object without name.
        """
        response = self.create_shop()
        url = '/api/v1/shops/{}'.format(response.data['slug'])
        data = {
            'user': self.commom_user.id
        }
        response = self.client.put(url, data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.commom_user_token))
        self.assertEqual(response.status_code, 400)

    def test_update_shop_with_invalid_user(self):
        """
        Ensure we can't update a shop object with invalid user.
        """
        response = self.create_shop()
        url = '/api/v1/shops/{}'.format(response.data['slug'])
        data = {
            'name': 'Test Shop Updated',
            'user': 'invalid'
        }
        response = self.client.put(url, data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.commom_user_token))
        self.assertEqual(response.status_code, 400)

    def test_update_shop_with_not_exists_user(self):
        """
        Ensure we can't update a shop object with not exists user.
        """
        response = self.create_shop()
        url = '/api/v1/shops/{}'.format(response.data['slug'])
        data = {
            'name': 'Test Shop Updated',
            'user': 99999
        }
        response = self.client.put(url, data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.commom_user_token))
        self.assertEqual(response.status_code, 400)

    def test_update_shop_without_authentication(self):
        """
        Ensure we can't update a shop object without authentication.
        """
        response = self.create_shop()
        url = '/api/v1/shops/{}'.format(response.data['slug'])
        data = {
            'name': 'Test Shop Updated',
            'user': self.commom_user.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 401)

    def test_update_shop_with_invalid_slug(self):
        """
        Ensure we can't update a shop object with invalid slug.
        """
        response = self.create_shop()
        url = '/api/v1/shops/invalid'
        data = {
            'name': 'Test Shop Updated',
            'user': self.commom_user.id
        }
        response = self.client.put(url, data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.commom_user_token))
        self.assertEqual(response.status_code, 404)

    def test_delete_shop(self):
        """
        Ensure we can delete a shop object.
        """
        response = self.create_shop()
        url = '/api/v1/shops/{}'.format(response.data['slug'])
        response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.admin_user_token))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Shop.objects.count(), 0)

    def test_delete_shop_without_permission(self):
        """
        Ensure we can't delete a shop object without permission.
        """
        response = self.create_shop()
        url = '/api/v1/shops/{}'.format(response.data['slug'])
        response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.commom_user_token))
        self.assertEqual(response.status_code, 403)

    def test_delete_shop_with_invalid_slug(self):
        """
        Ensure we can't delete a shop object with invalid slug.
        """
        url = '/api/v1/shops/invalid'
        response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.admin_user_token))
        self.assertEqual(response.status_code, 404)


class ProductTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='a2d4g6j8')
        self.shop = Shop.objects.create(name='Test Shop', user=self.user)
        self.category = Category.objects.create(name='Test Category')
        self.base_url = '/api/v1/products'
        self.token = self.login().data['access']

    def login(self):
        url = '/api/v1/jwt/create/'
        data = {
            'username': 'testuser',
            'password': 'a2d4g6j8'
        }
        response = self.client.post(url, data, format='json')
        return response

    def create_product(self):
        data = {
            'name': 'Test Product',
            'description': 'This is a test product.',
            'price': '10.00',
            'shop': self.shop.id,
            'category': self.category.id
        }
        return self.client.post(self.base_url, data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))

    def test_create_product(self):
        """
        Ensure we can create a new product object.
        """
        response = self.create_product()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], 'Test Product')
        self.assertEqual(response.data['description'], 'This is a test product.')
        self.assertEqual(response.data['price'], '10.00')
        self.assertEqual(response.data['shop'], self.shop.id)
        self.assertEqual(response.data['category'], self.category.id)

    def test_create_product_without_authentication(self):
        """
        Ensure we can't create a new product object without authentication.
        """
        data = {
            'name': 'Test Product',
            'description': 'This is a test product.',
            'price': '10.00',
            'shop': self.shop.id,
            'category': self.category.id
        }
        response = self.client.post(self.base_url, data, format='json')
        self.assertEqual(response.status_code, 401)

    def test_list_products(self):
        """
        Ensure we can list all products.
        """
        response = self.client.get(self.base_url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_retrieve_product(self):
        """
        Ensure we can retrieve a product object.
        """
        response = self.create_product()
        url = '/api/v1/products/{}'.format(response.data['slug'])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Test Product')
        self.assertEqual(response.data['description'], 'This is a test product.')
        self.assertEqual(response.data['price'], '10.00')
        self.assertEqual(response.data['shop'], self.shop.id)
        self.assertEqual(response.data['category'], self.category.id)

    def test_retrieve_product_with_invalid_slug(self):
        """
        Ensure we can retrieve a product object with invalid slug.
        """
        url = '/api/v1/products/invalid'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_update_product(self):
        """
        Ensure we can update a product object.
        """
        response = self.create_product()
        url = '/api/v1/products/{}'.format(response.data['slug'])
        data = {
            'name': 'Updated Test Product',
            'description': 'This is an updated test product.',
            'price': '20.00',
            'shop': self.shop.id,
            'category': self.category.id
        }
        response = self.client.put(url, data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Updated Test Product')
        self.assertEqual(response.data['description'], 'This is an updated test product.')
        self.assertEqual(response.data['price'], '20.00')
        self.assertEqual(response.data['shop'], self.shop.id)
        self.assertEqual(response.data['category'], self.category.id)

    def test_update_product_without_authentication(self):
        """
        Ensure we can't update a product object without authentication.
        """
        response = self.create_product()
        url = '/api/v1/products/{}'.format(response.data['slug'])
        data = {
            'name': 'Updated Test Product',
            'description': 'This is an updated test product.',
            'price': '20.00',
            'shop': self.shop.id,
            'category': self.category.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 401)

    def test_update_product_with_invalid_slug(self):
        """
        Ensure we can't update a product object with invalid slug.
        """
        url = '/api/v1/products/invalid'
        data = {
            'name': 'Updated Test Product',
            'description': 'This is an updated test product.',
            'price': '20.00',
            'shop': self.shop.id,
            'category': self.category.id
        }
        response = self.client.put(url, data, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        self.assertEqual(response.status_code, 404)

    def test_delete_product(self):
        """
        Ensure we can delete a product object.
        """
        response = self.create_product()
        url = '/api/v1/products/{}'.format(response.data['slug'])
        response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, None)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, None)

    def test_delete_product_without_authentication(self):
        """
        Ensure we can't delete a product object without authentication.
        """
        response = self.create_product()
        url = '/api/v1/products/{}'.format(response.data['slug'])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 401)

    def test_delete_product_with_invalid_slug(self):
        """
        Ensure we can't delete a product object with invalid slug.
        """
        url = '/api/v1/products/invalid'
        response = self.client.delete(url, format='json', HTTP_AUTHORIZATION='JWT {}'.format(self.token))
        self.assertEqual(response.status_code, 404)
