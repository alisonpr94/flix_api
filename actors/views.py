from rest_framework import generics
from .models import Actors
from .serializers import ActorsSerializer

class ActorsCreateListView(generics.ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer

class ActorsDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer