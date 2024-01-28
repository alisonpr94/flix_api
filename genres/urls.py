from django.urls import path
from .views import GenreCreateListView, GenreDetailUpdateDeleteView


urlpatterns = [
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>', GenreDetailUpdateDeleteView.as_view(), name='genre-detail-view'),
]
