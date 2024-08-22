from django.urls import path
from autenticacao.views import (
    do_login, 
    do_logout
)

urlpatterns = [
    path('', do_login, name='do_login'),
    path('logout', do_logout, name='do_logout')
]
    