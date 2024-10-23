from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('notes/',views.NoteAPI.as_view()),
    path('notes/<int:pk>/', views.NoteAPI.as_view()),  # For GET (detail), PUT, PATCH, DELETE

]
