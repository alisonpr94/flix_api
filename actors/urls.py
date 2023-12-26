from django.urls import path
from .views import ActorsCreateListView, ActorsDetailUpdateDeleteView


urlpatterns = [
    path('actors/', ActorsCreateListView.as_view(), name='actors-create-list'),
    path('actors/<int:pk>', ActorsDetailUpdateDeleteView.as_view(), name='actors-detail-view'),
]