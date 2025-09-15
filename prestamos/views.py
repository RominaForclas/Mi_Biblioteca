from django.shortcuts import render, get_object_or_404
from .models import Libro


def index(request):
    total_libros = Libro.objects.count()
    dispopnibles = Libro.objects.filter(disponible=True).count()
    return render(request, 'prestamos/index.html', context={'total_libros': total_libros, 'disponibles': dispopnibles})

def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'prestamos/libro_list.html', context={'libros': libros})

def libro_detail(request, pk):
    libro_instance = get_object_or_404(Libro, pk=pk)
    return render(request, 'prestamos/libro_detail.html', context={'libro': libro_instance})

# Create your views here.
