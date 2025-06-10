from django.shortcuts import render

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