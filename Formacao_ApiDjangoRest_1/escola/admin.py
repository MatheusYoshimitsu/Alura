from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nasc')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Aluno, Alunos) # model e configuracao do model

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'cod_curso', 'descricao')
    list_display_links = ('id', 'cod_curso')
    search_fields = ('cod_curso',)

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id', )

admin.site.register(Matricula, Matriculas)