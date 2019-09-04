from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome_aluno = models.CharField(
        max_length=50,
    )    

    idade_aluno = models.CharField(
        max_length=3,
    )

    email_aluno = models.CharField(
        max_length=50,
    )
    
    def __str__(self):
        return self.nome_aluno