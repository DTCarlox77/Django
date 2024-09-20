from django.urls import path
from .views import main, usuario, busqueda

urlpatterns = [
    path('', main, name='main'),
    path('user/<str:nombre>/', usuario, name='user'),
    path('search/', busqueda, name='search')
]
