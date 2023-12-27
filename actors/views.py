from rest_framework import generics
from .models import Actor
from .serializers import ActorSerializer
from rest_framework.permissions import IsAuthenticated

class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer