from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def publicacoes(request):
    return render(request, 'publicacoes.html')

def guia(request):
    return render(request, 'guia.html')

def loja(request):
    return render(request, 'loja.html')

