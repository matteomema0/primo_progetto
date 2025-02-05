from django.urls import path
from .views import home , articoloDetailView,index3,listaArticoli
app_name = 'news'

urlpatterns = [
    path('', home, name="homepage"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path('index3', index3, name="index3"),
    path('listaArticoli', listaArticoli, name="listaArticoli"),   
]
