from django.urls import path
from .views import genre_create_list_view, genre_detail_view

urlpatterns = [
    path('genres/', genre_create_list_view, name='genre-create-list'),
    path('genres/<int:pk>', genre_detail_view, name='genre-detail-view'),
]