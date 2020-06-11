from django.urls import path

from AnimeList import views

urlpatterns = [
    path('', views.index, name='index'),
    path('watchanime', views.watchanime, name='watchanime'),
    path('animes', views.animes, name='animelist'),
    path('searchanime', views.searchanime, name='searchanime'),
    path('topanime', views.top_anime, name='topanime'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('onepiece/Episode/<int:ep_no>', views.one_piece, name='onepiece'),
    path('naruto/Episode/<int:ep_no>', views.naruto_, name='naruto'),
]
