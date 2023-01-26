from django.urls import path
from . import views

app_name = 'turmas'

urlpatterns = [
    path('', views.turmas, name='turmas'),
    path('novopost', views.criarPost, name="criarPost"),
    path('participar', views.participar, name="participar"),
    path('criar', views.criar, name="criar"),
    path('<str:codigo>', views.turmas, name='turmas'),
]