from django.urls import path

from clients import views

urlpatterns = [
    path('', views.clients, name='clients'),
]