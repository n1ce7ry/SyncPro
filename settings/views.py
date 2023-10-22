from django.shortcuts import render
from django.utils import timezone

from settings.services.services import get_user_data


def settings_view(request):
    context = get_user_data(request.user.id)
    context["now"] = timezone.now()
    return render(request, 'settings/settings.html', context=context)