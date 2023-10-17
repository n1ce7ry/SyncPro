from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.utils import timezone

from clients.models import Client


class ClientsListView(ListView):
    model = Client
    paginate_by = 20 
    template_name = 'clients/clients.html'
    ordering = ['-created_at']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return _get_todays_date(context)


class AddClientView(CreateView):
    model = Client
    fields = ['name', 'phone', 'email']
    template_name = 'clients/addclient.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return _get_todays_date(context)

    
class EditClientView(UpdateView):
    model = Client
    fields = ['name', 'phone', 'email']
    template_name = 'clients/editclient.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return _get_todays_date(context)


def _get_todays_date(context):
    context["now"] = timezone.now()
    return context
