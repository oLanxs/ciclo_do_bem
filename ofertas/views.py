# ofertas/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.utils import timezone
from .models import Oferta
from .forms import OfertaForm

@login_required
def listar_ofertas(request):
    """Página que lista todas as ofertas disponíveis para instituições"""
    if request.user.tipo != "instituicao":
        return HttpResponseForbidden("Apenas instituições podem visualizar as ofertas.")

    hoje = timezone.now()
    palavra_chave = request.GET.get("q", "")
    horas = request.GET.get("horas", "")

    ofertas = Oferta.objects.filter(status="disponivel", data_expiracao__gt=hoje)

    if palavra_chave:
        ofertas = ofertas.filter(titulo__icontains=palavra_chave)

    if horas.isdigit():
        limite = hoje + timezone.timedelta(hours=int(horas))
        ofertas = ofertas.filter(data_expiracao__lte=limite)

    return render(request, "ofertas/listar.html", {"ofertas": ofertas})

@login_required
def criar_oferta(request):
    """Página para estabelecimentos criarem novas ofertas"""
    if request.user.tipo != "estabelecimento":
        return HttpResponseForbidden("Apenas estabelecimentos podem criar ofertas.")

    if request.method == "POST":
        form = OfertaForm(request.POST, request.FILES)
        if form.is_valid():
            oferta = form.save(commit=False)
            oferta.estabelecimento = request.user
            oferta.save()
            return redirect("listar_ofertas")
    else:
        form = OfertaForm()

    return render(request, "ofertas/form.html", {"form": form})
