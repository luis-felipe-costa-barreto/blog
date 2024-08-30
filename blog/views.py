from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    context = {
        'interesses': Interesses.objects.all(), 'cursos': Cursos.objects.all(), 'jogos': Jogos_favoritos.objects.all()
    }
    return render (request, 'index.html', context)

def sobre(request):
    context = {
        'cursos': Cursos.objects.all()
    }
    return render (request, 'sobre.html', context)