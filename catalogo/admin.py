from django.contrib import admin
from .models import Genero, Filme


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'ano_lancamento',
        'nota',
        'disponivel',
        'genero',
    )

    search_fields = ('titulo',)
    list_filter = ('disponivel', 'ano_lancamento', 'genero')