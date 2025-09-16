from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USUARIO_CHOICES = (
        ('estabelecimento', 'Estabelecimento'),
        ('instituicao', 'Instituição'),
    )

    username = None  # removendo username padrão
    email = models.EmailField(unique=True, verbose_name="Email")

    tipo = models.CharField(
        max_length=20,
        choices=USUARIO_CHOICES,
        verbose_name="Tipo de usuário"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["tipo"]

    def __str__(self):
        return f"{self.email} ({self.get_tipo_display()})"
