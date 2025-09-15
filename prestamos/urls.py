from django.urls import path
from . import views

app_name = 'prestamos'

urlpatterns = [
    path('', views.index, name='index'),
    path('libros/', views.libro_list, name='libro_list'),
    path('libro/<int:pk>/', views.libro_detail, name='libro_detail'),
]