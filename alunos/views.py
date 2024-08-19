from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Aluno
from .forms import AlunoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def do_login(request):
    if request.POST:
        username = request.POST['usuario']
        password = request.POST['senha']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return inicial(request)

    return render(request, 'alunos/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def inicial(request):
    
    alunos = Aluno.objects.all().order_by('nome')
    # select * from alunos_aluno;
    return render(request, 'alunos/index.html', context={'alunos': alunos})

@login_required
def detalhe_aluno(request, pk):
   
    aluno = Aluno.objects.get(id=pk)
    # select * from alunos_aluno where id = pk
    return render(request, 'alunos/detalhe.html', context={'aluno': aluno})

@login_required
def excluir_aluno(request, pk):
    
    aluno = Aluno.objects.get(id=pk)
    aluno.delete()
    # delete from alunos_aluno where id = pk
    
    return inicial(request)

@login_required
def criar_aluno(request):
    
    if request.method == 'POST':
        aluno_form = AlunoForm(request.POST)
        
        if aluno_form.is_valid():
            aluno_form.save()
            # insert into alunos_aluno (nome, nascimento, sobre) values ();
    
            return inicial(request)
        else:
            messages.error(request, aluno_form.errors)
    
    form = AlunoForm()
    return render(request, 'alunos/form_novo.html', context={'form': form})

@login_required
def editar_aluno(request, pk):
    
    aluno = Aluno.objects.get(id=pk)
    if request.method == 'POST':
        aluno_form = AlunoForm(request.POST, instance=aluno)
        
        if aluno_form.is_valid():
            aluno_form.save()
            # insert into alunos_aluno (nome, nascimento, sobre) values ();
    
            return inicial(request)
    
    form = AlunoForm(instance=aluno)
    return render(request, 'alunos/form_edicao.html', context={'form': form, 'aluno': aluno})