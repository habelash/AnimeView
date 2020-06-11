from django.contrib import admin
from .models import animelist, topanime

# Register your models here.


class animename(admin.ModelAdmin):
    list_display = ('name', 'Discription')


admin.site.register(animelist, animename)
admin.site.register(topanime, animename)
