from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'loja/index.html')

def cadastro(request):
    return render(request, 'loja/cadastro.html')

def login_view(request):
    return render(request, 'loja/login.html')

def produtos(request):
    return render(request, 'loja/produtos.html')

def acompanhamento(request):
    return render(request, 'loja/acompanhamento.html')

def peca(request):
    return render(request, 'loja/peca.html')

def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        if User.objects.filter(username=nome).exists():
            messages.error(request, "Usuário já existe.")
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, "Usuário cadastrado com sucesso!")
        return redirect('login')

    return render(request, 'loja/cadastro.html')

def login_view(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        senha = request.POST.get("senha")

        user = authenticate(request, username=nome, password=senha)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Credenciais inválidas.")
            return redirect('login')

    return render(request, 'loja/login.html')