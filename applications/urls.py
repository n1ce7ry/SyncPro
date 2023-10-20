from django.contrib.auth.decorators import login_required
from django.urls import path

from applications import views

urlpatterns = [
    path('', login_required(views.ApplicationsListView.as_view()), name='applications'),
    path('<int:pk>/', login_required(views.EditApplicatioon.as_view()), name='edit_app'),
    path('add-application/',
         login_required(views.AddApplicationView.as_view()),
         name='add_application'),
    path('search/', login_required(views.SearchApplicationsListView.as_view()), name='search_app'),
]