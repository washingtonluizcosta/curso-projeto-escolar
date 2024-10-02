from django.shortcuts import (
    render,
    redirect
)
from django.contrib.auth import (
    authenticate, 
    login, 
    logout
)
from django.contrib.auth.models import User
from alunos.models import Aluno
from alunos.views import listar_alunos
from escola.models import Professor

def do_login(request):
    if request.POST:
        username = request.POST['usuario']
        password = request.POST['senha']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            try:
                aluno = Aluno.objects.get(user_id=user.id)
            except Aluno.DoesNotExist:
                professor = Professor.objects.get(user_id=user.id)
            except Exception:
                print('Não é aluno e não é professor')
                return redirect('do_login')

            return redirect('listar_alunos')

    return render(request, 'autenticacao/login.html')

def do_logout(request):
    logout(request)
    return redirect('do_login')

