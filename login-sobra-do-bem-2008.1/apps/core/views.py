from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):
    return render(request, 'core/index.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        senha = request.POST['senha']

        try:
            # Busca o usuário pelo email
            user_obj = User.objects.get(email=email)
            # Autentica usando o username vinculado ao email
            user = authenticate(request, username=user_obj.username, password=senha)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Email ou senha inválidos.")
                return redirect('login')
        except User.DoesNotExist:
            messages.error(request, "Email não encontrado.")
            return redirect('login')

    return render(request, 'core/login.html')

def cadastro(request):
    # Sua lógica de cadastro aqui
    return render(request, 'core/cadastro.html')
