from django.urls import path
from .views import MovieCreateListView, MovieDetailUpdateDeleteView, MovieStatsView


urlpatterns = [
    path('movies/', MovieCreateListView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>', MovieDetailUpdateDeleteView.as_view(), name='movie-detail-view'),
    path('movies/stats/', MovieStatsView.as_view(), name='movie-stats-view'),
]
