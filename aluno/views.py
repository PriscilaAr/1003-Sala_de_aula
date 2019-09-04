from django.shortcuts import render
from rest_framework import viewsets
from aluno.models import Aluno
from aluno.serializes import AlunoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializes_class = AlunoSerializer
    


# Create your views here.

# def index(request): 
    
#     if request.method == 'POST':
#         aluno = Aluno()
#         aluno.nome = request.POST.get('nome')
#         aluno.idade = request.POST.get('idade')
#         aluno.email = request.POST.get('email')
#         aluno.save()