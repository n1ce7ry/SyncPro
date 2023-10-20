from django.utils import timezone

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from clients.models import Client
from clients.services.services import search_clients


class ClientsListView(ListView):
    model = Client
    template_name = 'clients/clients.html'
    paginate_by = 11 
    ordering = ['-created_at']
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return _get_todays_date(context)


class SearchClientsListView(ListView):
    model = Client
    template_name = 'clients/clients.html'
    paginate_by = 11
    
    def get_queryset(self):
        query = self.request.GET.get("q").strip()
        return search_clients(query)

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