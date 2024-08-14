from django.contrib import admin
from .models import Aluno
# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Aluno
        
admin.site.register(Aluno, AlunoAdmin)