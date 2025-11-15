from django.test import TestCase
from django.contrib.auth.models import User

class TesteLoginSenhaErrada(TestCase):
    def setUp(self):
        User.objects.create_user(
            username='teste',
            password='senha_correta'
        )

    def test_login_com_senha_errada_deve_falhar(self):
        response = self.client.post('/login/', {
            'username': 'teste',
            'password': 'senha_errada'
        })

        session = self.client.session
        self.assertNotIn('_auth_user_id', session)
