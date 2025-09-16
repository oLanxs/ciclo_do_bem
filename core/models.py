from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USUARIO_CHOICES = (
        ('estabelecimento', 'Estabelecimento'),
        ('instituicao', 'Instituição'),
    )
    tipo = models.CharField(
        max_length=20,
        choices=USUARIO_CHOICES,
        verbose_name="Tipo de usuário"
    )

    def __str__(self):
        return f"{self.username} ({self.get_tipo_display()})"
