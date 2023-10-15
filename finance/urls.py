from django.urls import path

from finance import views

urlpatterns = [
    path('', views.finance, name='finance'),
]