from django import forms
from .models import Oferta

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ["titulo", "descricao", "foto", "quantidade", "data_expiracao", "status"]
