from django.urls import path
from .views import (
    inicial,
    detalhe_aluno,
    excluir_aluno,
    criar_aluno,
    editar_aluno,
    do_login
)

urlpatterns = [
    path('login/', do_login, name='login'),
    path('', inicial, name='inicial'),
    path('criar/', criar_aluno, name='criar_aluno'),
    path('editar/<int:pk>/', editar_aluno, name='editar_aluno'),
    path('detalhe/<int:pk>/', detalhe_aluno, name='detalhe_aluno'),
    path('excluir/<int:pk>/', excluir_aluno, name='excluir_aluno'),
]