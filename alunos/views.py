from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Aluno
from .forms import AlunoForm
from django.contrib import messages

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

# Create your views here.
def inicial(request):
    alunos = Aluno.objects.all().order_by('nome')
    # select * from alunos_aluno;
    return render(request, 'alunos/index.html', context={'alunos': alunos})


def detalhe_aluno(request, pk):
    aluno = Aluno.objects.get(id=pk)
    # select * from alunos_aluno where id = pk
    return render(request, 'alunos/detalhe.html', context={'aluno': aluno})


def excluir_aluno(request, pk):
    aluno = Aluno.objects.get(id=pk)
    aluno.delete()
    # delete from alunos_aluno where id = pk
    
    return inicial(request)


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