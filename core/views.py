from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'core/index.html')


def login_estabelecimento(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None and user.tipo == 'estabelecimento':
            login(request, user)
            return redirect('dashboard_estabelecimento')  # redireciona para o dashboard
        else:
            messages.error(request, "Email ou senha inválidos ou tipo incorreto.")

    return render(request, 'core/login_estabelecimento.html')


def login_instituicao(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None and user.tipo == 'instituicao':
            login(request, user)
            return redirect('dashboard_instituicao')  # redireciona para o dashboard
        else:
            messages.error(request, "Email ou senha inválidos ou tipo incorreto.")

    return render(request, 'core/login_instituicao.html')


def logout_view(request):
    logout(request)
    return redirect('index')


# Páginas de dashboard
@login_required
def dashboard_estabelecimento(request):
    return render(request, 'core/dashboard_estabelecimento.html')


@login_required
def dashboard_instituicao(request):
    return render(request, 'core/dashboard_instituicao.html')
