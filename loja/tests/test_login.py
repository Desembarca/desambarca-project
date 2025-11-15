from django.test import TestCase
from django.contrib.auth.models import User

class TesteLoginAdmin(TestCase):
    def setUp(self):
        # cria o usuário correto
        User.objects.create_superuser(
            username='teste',
            email='teste@example.com',
            password='senha_correta'
        )

    def test_login_admin_deve_funcionar(self):
        # aqui propositalmente usamos a senha ERRADA
        response = self.client.post('/admin/login/?next=/admin/', {
            'username': 'teste',
            'password': 'senha_correta'   # senha errada proposital
        })

        # o teste espera que o login funcione (MAS NÃO VAI FUNCIONAR)
        # então o Jenkins VAI falhar — exatamente o que você quer
        self.assertEqual(response.status_code, 302)
        self.assertIn('_auth_user_id', self.client.session)
