from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'core/index.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        senha = request.POST['senha']
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Email ou senha inválidos.")
            return redirect('login')
    return render(request, 'core/login.html')

def cadastro(request):
    # Sua lógica de cadastro aqui
    return render(request, 'core/cadastro.html')
