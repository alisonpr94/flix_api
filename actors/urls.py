from django.urls import path
from .views import ActorCreateListView, ActorDetailUpdateDeleteView

urlpatterns = [
    path('actors/', ActorCreateListView.as_view(), name='actors-create-list'),
    path('actors/<int:pk>', ActorDetailUpdateDeleteView.as_view(), name='actors-detail-view'),
]