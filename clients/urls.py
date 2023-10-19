from django.urls import path
from django.contrib.auth.decorators import login_required

from clients import views

urlpatterns = [
    path('', login_required(views.ClientsListView.as_view()), name='clients'),
    path('add-client/', login_required(views.AddClientView.as_view()), name='add_client'),
    path('<int:pk>/', login_required(views.EditClientView.as_view()), name='edit_client'),
    path('search/', login_required(views.SearchClientsListView.as_view()), name='search_clients'),
]
