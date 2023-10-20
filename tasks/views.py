from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from tasks.models import Task
from tasks.services.services import tasks_filtering_by_status


class TasksListView(ListView):
    model = Task
    paginate_by = 16 
    template_name = 'tasks/tasks.html'
    ordering = ['-created_at'] 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return _get_todays_date(context)


class AddTaskView(CreateView):
    model = Task
    fields = ['title', 'description']
    template_name = 'tasks/newtask.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return _get_todays_date(context)

    
class EditTaskView(UpdateView):
    model = Task
    fields = ['title', 'description', 'status']
    template_name = 'tasks/edittask.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return _get_todays_date(context)


class DeleteTaskView(DeleteView):
    model = Task
    success_url = reverse_lazy("tasks")
    
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class FilterTasksListView(ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    paginate_by = 16
    
    def get_queryset(self):
        query = self.request.GET.get('status')
        return tasks_filtering_by_status(query)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return _get_todays_date(context)

    
def _get_todays_date(context):
    context["now"] = timezone.now()
    return context
