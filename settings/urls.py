from django.urls import path
from django.contrib.auth.decorators import login_required

from settings import views

urlpatterns = [
    path('', login_required(views.settings_view), name='settings'),
]