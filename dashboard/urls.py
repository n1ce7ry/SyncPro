from django.contrib.auth.decorators import login_required
from django.urls import path
from dashboard import views

urlpatterns = [
    path('', login_required(views.dashboard), name='dashboard'),
]
