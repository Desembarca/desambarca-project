from django.test import TestCase
from django.contrib.auth.models import User

class TesteLoginAdminSenhaErrada(TestCase):
    def setUp(self):
        User.objects.create_superuser(
            username='teste',
            password='senha_correta',
            email='teste@example.com'
        )

    def test_login_admin_com_senha_errada(self):
        response = self.client.post('/admin/login/', {
            'username': 'teste',
            'password': 'senha_errada'
        })

        # Admin NUNCA loga com senha errada -> sessão não deve ter o usuário
        session = self.client.session
        self.assertNotIn('_auth_user_id', session)