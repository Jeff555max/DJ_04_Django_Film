from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_film, name='add_film'),
    path('films/', views.show_films, name='show_films'),
]