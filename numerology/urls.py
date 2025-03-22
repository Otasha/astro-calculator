from django.urls import path
from .views import pythagorean_square_view

urlpatterns = [
    path('pythagorean-square/', pythagorean_square_view, name='pythagorean_square'),
]
