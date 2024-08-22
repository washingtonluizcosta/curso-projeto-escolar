from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from alunos.views import listar_alunos

def do_login(request):
    if request.POST:
        username = request.POST['usuario']
        password = request.POST['senha']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('listar_alunos')

    return render(request, 'autenticacao/login.html')

def do_logout(request):
    logout(request)
    return redirect('do_login')