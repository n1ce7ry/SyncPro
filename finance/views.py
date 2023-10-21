from django.views.generic.list import ListView

from applications.models import Application
from finance.services.services import (
    get_finance_statistics,
    get_statistics_by_month,
)


class FinanceListView(ListView):
    model = Application
    template_name = 'finance/finance.html'
    paginate_by = 8
    
    def get_queryset(self):
        return get_finance_statistics()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = get_statistics_by_month(context)
        return context