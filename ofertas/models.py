# ofertas/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone

class Oferta(models.Model):
    STATUS_CHOICES = [
        ("disponivel", "Disponível"),
        ("indisponivel", "Indisponível"),
    ]

    estabelecimento = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # usa core.CustomUser
        on_delete=models.CASCADE,
        related_name="ofertas",
        limit_choices_to={"tipo": "estabelecimento"},
        verbose_name="Estabelecimento"
    )

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    foto = models.ImageField(upload_to="ofertas/", blank=True, null=True)
    quantidade = models.PositiveIntegerField()
    data_expiracao = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="disponivel")
    criado_em = models.DateTimeField(auto_now_add=True)

    def esta_disponivel(self):
        return self.status == "disponivel" and self.data_expiracao > timezone.now()

    def __str__(self):
        return f"{self.titulo} - {self.estabelecimento.email}"
