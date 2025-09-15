from django.contrib import admin
from .models import Autor, Libro, Prestamo

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_nacimiento')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'disponible')
    list_filter = ('disponible', 'autor')
    search_fields = ('titulo',)

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('libro', 'usuario', 'fecha_prestamo', 'fecha_devolucion')
    list_filter = ('fecha_prestamo', 'fecha_devolucion')
