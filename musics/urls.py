from django.urls import path
from . import views

urlpatterns = [
    path('musics/', views.music_list),
    ]