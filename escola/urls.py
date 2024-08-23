from django.urls import path
from escola.views import painel

urlpatterns = [
    path('', painel, name='painel'),
]
    