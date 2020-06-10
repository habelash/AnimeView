from django.urls import path

from AnimeList import views

urlpatterns = [
    path('', views.index, name='index'),
    path('watchanime', views.watchanime, name='watchanime'),
    path('animelist', views.animelist, name='animelist'),
    path('searchanime', views.searchanime, name='searchanime'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('onepiece/Episode/<int:ep_no>', views.one_piece, name='onepiece'),
]
