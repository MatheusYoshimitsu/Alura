from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nasc = models.DateField()

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )

    cod_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao
    
class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
        ('I', 'Integral')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE) # Deleta a matricula caso aluno seja deletado
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE) # Deleta o curso caso aluno seja deletado
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')