from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, tipo=None, **extra_fields):
        if not email:
            raise ValueError("O campo Email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, tipo=tipo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, tipo="estabelecimento", **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superusuário precisa ter is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superusuário precisa ter is_superuser=True.")

        return self.create_user(email, password, tipo, **extra_fields)


class CustomUser(AbstractUser):
    USUARIO_CHOICES = (
        ("estabelecimento", "Estabelecimento"),
        ("instituicao", "Instituição"),
    )

    username = None  # removendo username
    email = models.EmailField(unique=True, verbose_name="Email")

    tipo = models.CharField(
        max_length=20,
        choices=USUARIO_CHOICES,
        verbose_name="Tipo de usuário"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["tipo"]

    objects = CustomUserManager()  # <<< IMPORTANTE

    def __str__(self):
        return f"{self.email} ({self.get_tipo_display()})"
