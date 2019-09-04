from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome_aluno = models.CharField(
        max_length=255,
    )    

    idade_aluno = models.IntegerField(
        max_length=4,
    )

    email_aluno = models.EmailField(
        max_length=255,
    )
    
    def __str__(self):
        return self.nome_aluno