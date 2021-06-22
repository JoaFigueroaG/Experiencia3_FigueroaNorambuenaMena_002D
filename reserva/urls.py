from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from .import views 


urlpatterns=[
    path('', views.menu, name='menu'),
    path('simple/', views.simple, name='simple'),
    path('formulario/', views.formulario, name='formulario'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    #path('login/', LoginView, {'template_name':'login.html'}, name = 'login'),

]