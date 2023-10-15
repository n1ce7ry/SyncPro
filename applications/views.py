from django.shortcuts import render


def applications(request):
    return render(request, 'applications/applications.html')
