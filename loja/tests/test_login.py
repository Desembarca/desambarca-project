from django.test import TestCase
from django.contrib.auth.models import User

class TesteLoginQueDeveFalhar(TestCase):
    def setUp(self):
        User.objects.create_user(
            username='teste',
            password='senha_correta'
        )

    def test_login_deve_funcionar(self):
        # Aqui você testa usando senha ERRADA de propósito
        response = self.client.post('/admin/login/', {
            'username': 'teste',
            'password': 'senha_correta'
        })

        # Pega a sessão após a tentativa de login
        session = self.client.session

        # O teste espera que o login funcione (MAS NÃO VAI FUNCIONAR)
        self.assertIn(
            '_auth_user_id',
            session,
            'O login deveria funcionar, mas falhou.'
        )
