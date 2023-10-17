from django.urls import path

from clients import views

urlpatterns = [
    path('', views.ClientsListView.as_view(), name='clients'),
    path('add-client/', views.AddClientView.as_view(), name='add_client'),
    path('<int:pk>/', views.EditClientView.as_view(), name='edit_client'),
]
