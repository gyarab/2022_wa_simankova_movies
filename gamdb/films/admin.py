from django.contrib import admin

from .models import Movie, Director, Genre

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year', 'director', 'genres_display']
    list_display_links = ['name']
    search_fields = ['name']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Director)
admin.site.register(Genre)
# asdf