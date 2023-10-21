from django.urls import path
from django.contrib.auth.decorators import login_required

from finance import views

urlpatterns = [
    path('', login_required(views.FinanceListView.as_view()), name='finance'),
]