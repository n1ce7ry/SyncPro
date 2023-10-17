from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView

from tasks.models import Task


class TasksListView(ListView):
    model = Task
    paginate_by = 20 
    template_name = 'tasks/tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


def tasks(request):
    return render(request, 'tasks/tasks.html')
