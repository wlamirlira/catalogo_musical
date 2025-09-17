#from django.urls import path
#from . import views

#urlpatterns = [
#    path('', views.index, name='index'),
#    path('adicionar/', views.adicionar_musica, name='adicionar_musica'),
#    path('editar/<int:id>/', views.editar_musica, name='editar_musica'),
#    path('deletar/<int:id>/', views.deletar_musica, name='deletar_musica'),
#]


# musicas/urls.py
from django.urls import path
from . import views

app_name = 'musicas'

urlpatterns = [
    path('', views.index, name='index'),
    path('nova/', views.adicionar_musica, name='adicionar_musica'),
    path('<int:pk>/editar/', views.editar_musica, name='editar_musica'),
    path('<int:pk>/excluir/', views.deletar_musica, name='deletar_musica'),
]
