from django.shortcuts import render
from .models import Midia

def index(request):
    midias_publicadas = Midia.objects.filter(Publicada=True).order_by('-Data_de_publicação')
    return render(request, 'midia/index.html', {'midias_publicadas': midias_publicadas})
