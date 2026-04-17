from django.urls import path
from .views import AddBookAPIView, GetBookAPIView, UpdateBookAPIView, DeleteBookAPIView


urlpatterns = [
    path('add-book/', AddBookAPIView.as_view(), name='add-book'), # tested
    path('get-book/', GetBookAPIView.as_view(), name='get-book'), # tested
    path('update-book/<int:pk>/', UpdateBookAPIView.as_view(), name='update-book'), # tested
    path('delete-book/<int:pk>/', DeleteBookAPIView.as_view(), name='delete-book'), # tested
]

