from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class RealLoginTest(TestCase):
    # O método 'setUp' é executado antes de cada teste
    def setUp(self):
        # 1. Dados para o usuário
        self.username = 'usuarioteste'
        self.password = 'SenhaSegura123'
        self.login_url = reverse('login') # Assume que você tem uma URL nomeada 'login'
        
        # 2. Cria e salva o usuário no banco de dados de teste
        self.user = User.objects.create_user(
            username=self.username, 
            password=self.password
        )

    # --- TESTE 1: SUCESSO ---
    def test_successful_login(self):
        """Testa o login com credenciais corretas."""
        
        # Dados do formulário
        credentials = {
            'username': self.username,
            'password': self.password, # Senha CORRETA
        }
        
        # Envia a requisição POST para a URL de login
        response = self.client.post(self.login_url, credentials, follow=True)
        
        # Verifica se o login foi bem-sucedido:
        # Geralmente, um login bem-sucedido resulta em um redirecionamento (código 302),
        # que o 'follow=True' segue e retorna 200 para a página de destino (ex: home).
        
        self.assertEqual(response.status_code, 200)
        
        # Opcional: Verifica se o usuário foi realmente autenticado na sessão
        self.assertTrue('_auth_user_id' in self.client.session)
        
        print("\n[Sucesso] Login com credenciais corretas passou.")


    # --- TESTE 2: FALHA ---
    def test_failed_login_bad_password(self):
        """Testa o login com senha incorreta."""
        
        # Dados do formulário
        credentials = {
            'username': self.username,
            'password': 'senha_totalmente_errada', # Senha INCORRETA
        }
        
        # Envia a requisição POST para a URL de login
        response = self.client.post(self.login_url, credentials, follow=True)
        
        # Verifica se o login falhou:
        # Um login fracassado NÃO deve autenticar o usuário nem redirecionar.
        # Ele deve permanecer na página de login e retornar status 200.
        
        self.assertEqual(response.status_code, 200)
        
        # Opcional: Verifica se o usuário NÃO foi autenticado na sessão
        self.assertTrue('_auth_user_id' not in self.client.session)
        
        # Opcional: Verifica se a mensagem de erro está presente (se implementada)
        # self.assertContains(response, 'Usuário ou senha inválidos')
        
        print("\n[Falha] Login com senha incorreta passou na verificação de falha.")