from django.urls import path 
from .views import index4,view_a,view_b,view_c,view_d,view_e,view_f
app_name = 'Corsi_di_Formazioane'

urlpatterns = [
    path('view_a',view_a,name='Lista dei Corsi'),
    path('view_b',view_b,name='Dettagli dei Corsi'),
    path('view_c',view_c,name='Corsi che iniziano dopo il 01/05/2025'),
    path('view_d',view_d,name='Corsi con meno di 20 posti disponibili'),
    path('view_e',view_e,name='Corsi che terminano entro il 30/04/2025'),
    path('view_f',view_f,name='Statistiche Avanzate sui Corsi'),   
    path('index4',index4,name='index4'), 
]
