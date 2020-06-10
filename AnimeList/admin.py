from django.contrib import admin
from .models import onepiece

# Register your models here.
admin.site.site_header = 'Anime View'


class AnimeListAdmin(admin.ModelAdmin):
    list_display = ('Episode', 'EpisodeLink')
    list_display_links = ('Episode', 'EpisodeLink')


admin.site.register(onepiece, AnimeListAdmin)
