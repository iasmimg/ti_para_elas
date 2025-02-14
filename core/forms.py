from django.forms import ModelForm
from .models import Acao

class AcaoForm(ModelForm):
    class Meta:
        model = Acao
        fields = ['titulo', 'descricao', 'autor', 'tipo', 'imagem', 'linkgeral', 'linkms']