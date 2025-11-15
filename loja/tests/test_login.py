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
            'password': 'senha_correta'
        })

        session = self.client.session

        # ESTE TESTE VAI FALHAR DE PROPÓSITO
        self.assertIn(
            '_auth_user_id',
            session,
            "Falha proposital: senha errada não deveria logar."
        )
