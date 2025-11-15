from django.test import TestCase
from django.urls import reverse

class LoginTest(TestCase):
    def test_login_page_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_valid_user(self):
        # cria usuário
        from django.contrib.auth.models import User
        User.objects.create_user(username='paulo', password='123456')

        # tenta logar
        response = self.client.post(reverse('login'), {
            'username': 'paulo',
            'password': '123456'
        })

        # deve redirecionar (login OK)
        self.assertEqual(response.status_code, 302)
