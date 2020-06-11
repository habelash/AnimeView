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
    path('haikyu/Episode/<int:ep_no>', views.haikyuu, name='haikyu'),
    path('attackontitans/Episode/<int:ep_no>', views.attackontitans, name='attackontitans'),
    path('myheroaccademy/Episode/<int:ep_no>', views.myheroaccademy, name='myheroaccademy'),
    path('onepunchman/Episode/<int:ep_no>', views.onepunchmann, name='onepunchman'),
    path('afrosamurai/Episode/<int:ep_no>', views.afro_samurai, name='afrosamurai'),
    path('bleach/Episode/<int:ep_no>', views.blleach, name='bleach'),
    path('deathnote/Episode/<int:ep_no>', views.death_note, name='deathnote'),
    path('fairytail/Episode/<int:ep_no>', views.fairy_tail, name='fairytail'),
    path('fullmetalalcamist/Episode/<int:ep_no>', views.full_metal_alcamist, name='fullmetalalcamist'),
    path('hunterXhunter/Episode/<int:ep_no>', views.hunterxhunter, name='hunterXhunter'),
    path('tokyoghoul/Episode/<int:ep_no>', views.tokyo_ghoul, name='tokyoghoul'),
    path('boruto/Episode/<int:ep_no>', views.borutoo, name='boruto'),
]
