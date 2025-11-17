from django.test import TestCase
from django.contrib.auth.models import User

class TesteLoginAdmin(TestCase):
    
    def setUp(self):
        User.objects.create_superuser(
            username='teste',
            email='teste@example.com',
            password='senha_correta'
        )

    def test_login(self):
        
        response = self.client.post('/admin/login/?next=/admin/', {
            'username': 'teste',
            'password': 'senha_correta  '   
        })

        
        self.assertEqual(response.status_code, 302)
        self.assertIn('_auth_user_id', self.client.session)
