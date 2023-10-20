from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from applications.models import Application
from applications.services.services import search_applications


class ApplicationsListView(ListView):
    model = Application
    template_name = 'applications/applications.html'
    paginate_by = 11 
    ordering = ['-created_at'] 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return _get_todays_date(context)


class SearchApplicationsListView(ListView):
    model = Application
    template_name = 'applications/applications.html'
    paginate_by = 11
    
    def get_queryset(self):
        query = self.request.GET.get("q").strip()
        return search_applications(query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return _get_todays_date(context)


class AddApplicationView(CreateView):
    model = Application
    fields = ['client', 'title', 'price']
    template_name = 'applications/newapplication.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return _get_todays_date(context)

    
class EditApplicatioon(UpdateView):
    model = Application
    fields = ['title', 'client', 'price']
    template_name = 'applications/editapplication.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return _get_todays_date(context)


def _get_todays_date(context):
    context["now"] = timezone.now()
    return context