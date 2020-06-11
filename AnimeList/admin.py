from django.contrib import admin
from .models import onepiece, naruto, afrosamurai, aot, bleach, \
    bnha, deathnote, fairytail, fmab, haikyu, hxh, kny, onepunchman

admin.site.site_header = 'Anime View'


# Register your models here.

class AnimeListAdmin(admin.ModelAdmin):
    list_display = ('Episode', 'EpisodeLink')
    list_display_links = ('Episode', 'EpisodeLink')


admin.site.register(onepiece, AnimeListAdmin)
admin.site.register(naruto, AnimeListAdmin)
admin.site.register(afrosamurai, AnimeListAdmin)
admin.site.register(aot, AnimeListAdmin)
admin.site.register(bnha, AnimeListAdmin)
admin.site.register(bleach, AnimeListAdmin)
admin.site.register(deathnote, AnimeListAdmin)
admin.site.register(fairytail, AnimeListAdmin)
admin.site.register(fmab, AnimeListAdmin)
admin.site.register(haikyu, AnimeListAdmin)
admin.site.register(hxh, AnimeListAdmin)
admin.site.register(kny, AnimeListAdmin)
admin.site.register(onepunchman, AnimeListAdmin)
