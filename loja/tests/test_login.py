from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TesteLoginSenhaErrada(TestCase):

    def setUp(self):
        # Usuário REAL com senha real
        self.user = User.objects.create_user(
            username="teste",
            password="senha_correta"
        )

    def test_login_com_senha_errada_deve_falhar(self):
        # Faz login com SENHA ERRADA propositalmente
        response = self.client.post(
            reverse('login'),
            {
                'username': 'teste',
                'password': 'senha_errada'
            }
        )

        # O login com senha errada NÃO autentica,
        # então a sessão continua SEM o id de usuário logado.
        # Mas aqui vamos esperar que o login dê certo de propósito.
        
        self.assertIn(
            '_auth_user_id',
            self.client.session,
            "Falha proposital: senha errada não loga, este teste deve falhar."
        )
