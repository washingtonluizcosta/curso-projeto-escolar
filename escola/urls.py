from django.urls import path
from escola.views import painel
from .views import (
    listar_professores,
    detallhe_professor,
    excluir_professor,
    criar_professor,
    editar_professor
)

urlpatterns = [
    path('', listar_professores, name='listar_professores'),
    path('criar/', criar_professor, name='criar_prfessor'),
    path('editar/<int:pk>/', editar_professor, name='editar_prfessor'),
    path('detalhe/<int:pk>/', detallhe_professor, name='detalhe_professor'),
    path('excluir/<int:pk>/', excluir_professor, name='excluir_prfessor'),
]

    