from django.views.generic.list import ListView

from clients.models import Client
from dashboard.services.services import (
    get_customer_statistics,
    get_summarize_all_section,
)


class DashboardListView(ListView):
    model = Client
    template_name = 'dashboard/dashboard.html'

    def get_queryset(self):
        query = get_customer_statistics()
        return query
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return get_summarize_all_section(context)