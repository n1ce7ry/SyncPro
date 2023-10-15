from django.urls import path

from applications import views

urlpatterns = [
    path('', views.applications, name='applications'),
]