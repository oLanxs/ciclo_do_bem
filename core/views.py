from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    return render(request, 'core/index.html')


def login_estabelecimento(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        # Verifica se o usuário existe e se é do tipo estabelecimento
        if user is not None and user.tipo == 'estabelecimento':
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Email ou senha inválidos ou tipo incorreto.")

    return render(request, 'core/login_estabelecimento.html')


def login_instituicao(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        # Verifica se o usuário existe e se é do tipo instituição
        if user is not None and user.tipo == 'instituicao':
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Email ou senha inválidos ou tipo incorreto.")

    return render(request, 'core/login_instituicao.html')


def logout_view(request):
    logout(request)
    return redirect('index')
