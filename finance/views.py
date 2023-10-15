from django.shortcuts import render


def finance(request):
    return render(request, 'finance/finance.html')