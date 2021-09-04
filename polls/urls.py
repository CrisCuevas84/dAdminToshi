from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes', views.clientes, name='clientes'),
    path('sitios', views.sitios, name='sitios'),
    path('documentos', views.documentos, name='documentos'),
    path('oportunidades', views.oportunidades, name='oportunidades'),
]