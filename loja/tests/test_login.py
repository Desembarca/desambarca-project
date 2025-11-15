from django.test import TestCase
from django.contrib.auth.models import User

class TesteLoginAdmin(TestCase):
    def setUp(self):
        User.objects.create_user(
            username='teste',
            password='senha_correta'
        )

    def test_login_admin(self):
        response = self.client.post('/admin/login/?next=/admin/', {
            'username': 'teste',
            'password': 'senha_correta'
        })

        # Verifica a sessão
        session = self.client.session

        self.assertIn(
            '_auth_user_id', 
            session,
            'Login deveria ter funcionado, mas não funcionou.'
        )
