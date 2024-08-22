from django.urls import path
from .views import (
    listar_alunos,
    detalhe_aluno,
    excluir_aluno,
    criar_aluno,
    editar_aluno
)

urlpatterns = [
    path('', listar_alunos, name='listar_alunos'),
    path('criar/', criar_aluno, name='criar_aluno'),
    path('editar/<int:pk>/', editar_aluno, name='editar_aluno'),
    path('detalhe/<int:pk>/', detalhe_aluno, name='detalhe_aluno'),
    path('excluir/<int:pk>/', excluir_aluno, name='excluir_aluno'),
]