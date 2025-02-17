from rest_framework import viewsets
from .models import Acao
from .serializers import Acao

class AcaoViewSet(viewsets.ModelViewSet):
    queryset = Acao.objects.all()
    serializer_class = Acao