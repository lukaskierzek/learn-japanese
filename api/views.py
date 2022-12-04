from rest_framework import viewsets
from .serializer import WordsSerializer
from .models import Words


# Create your views here.
class WordsViewSet(viewsets.ModelViewSet):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer
