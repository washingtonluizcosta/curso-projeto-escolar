from django.contrib import admin
from .models import Professor
# Register your models here.
class ProfessorAdmin(admin.ModelAdmin):
    class Meta:
      model = Professor

admin.site.register(Professor, ProfessorAdmin)