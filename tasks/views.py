from django.shortcuts import render


def tasks(request):
    return render(request, 'tasks/tasks.html')
