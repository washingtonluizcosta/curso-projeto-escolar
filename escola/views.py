from pyexpat.errors import messages
from django.shortcuts import render

from escola.forms import ProfessorForm
from .models import Professor


# Create your views here.
def painel(request):
    pass


def listar_professores(request):
    professores = Professor.objects.all().order_by('nome')
    return render(request, 'professores/index.html', context={'professores': professores})

def criar_professor(request):
    if request.method == "POST":
        professor_form = ProfessorForm(request.POST)
        if professor_form.is_valid:
            professor_form.save()

            return listar_professores(request)

        else:
            messages.error(request, professor_form.errors)

def excluir_professor(request, pk):
    professor = Professor.objects.get(id = pk)
    professor.delete()

    return listar_professores(request)

def detallhe_professor(request, pk):
    professor = Professor.objects.get(id=pk)
    form = ProfessorForm(instance=professor)

    return render(request, 'professor/detalhe.html', context={'professor': professor, 'form': form})

def editar_professor(request, pk):
    professor = Professor.objects.get(id=pk)
    if request.method == 'POST':
        professor_form = ProfessorForm(request.POST, instance=professor)
        
        if professor_form.is_valid():
            professor_form.save()
            # insert into alunos_aluno (nome, nascimento, sobre) values ();
    
            return listar_professores(request)
    
    form = ProfessorForm(instance=professor)
    return render(request, 'professor/form_edicao.html', context={'form': form, 'professor': professor})