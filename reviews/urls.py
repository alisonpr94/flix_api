from django.urls import path
from .views import ReviewCreateListView, ReviewDetailUpdateDeleteView

urlpatterns = [
    path('reviews/', ReviewCreateListView.as_view(), name='reviews-create-list'),
    path('reviews/<int:pk>', ReviewDetailUpdateDeleteView.as_view(), name='reviews-detail-view'),
]