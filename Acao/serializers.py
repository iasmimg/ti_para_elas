from rest_framework import serializers
from .models import Acao

class Acao(serializers.ModelSerializer):
    class meta:
        model = Acao
        fields = ['titulo', 'descricao', 'autor', 'tipo', 'imagem', 'linkgeral','linkms']
