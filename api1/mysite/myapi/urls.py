from . import views
from django.urls import path


urlpatterns = [
    path('author/', views.AuthorView.as_view()),
    path('author/<int:pk>/', views.AuthorView.as_view()),

    path('genre/', views.GenreView.as_view()),
    path('genre/<int:pk>/', views.GenreView.as_view()),

    path('book/', views.BookView.as_view()),
    path('book/<int:pk>/', views.BookView.as_view()),


]
