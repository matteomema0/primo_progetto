from os import path
from django.urls import path
from forms_app.views import contatti,elimina_contatto,modifica_contatto,lista_contatti


app_name="forms_app"
urlpatterns = [
    path('contattaci/', contatti, name='contatti'),
    path('modifica_contatto/<int:pk>/', modifica_contatto, name='modifica-contatto'),
    path('elimina_contatto/<int:pk>/', elimina_contatto, name='elimina-contat'),
    path('lista_contatti/', lista_contatti, name='lista_contatti'),
]



