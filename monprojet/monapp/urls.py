from django.urls import path
from .views import bonjour, getAllPersonnes, DogListCreate

urlpatterns = [
    path('hello/', bonjour, name='hello'),
    path('all/', getAllPersonnes, name='allPersonne'),
    path('dogs', DogListCreate.as_view(), name="dog-list-create")
]
