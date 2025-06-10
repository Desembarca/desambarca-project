from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('cadastro/', views.cadastro, name='cadastro'),
 path('login/', views.login_view, name='login'),
 path('produtos/', views.produtos, name='produtos'),
 path('acompanhamento/', views.acompanhamento, name='acompanhamento'),
 path('peca/', views.peca, name='peca')
]
