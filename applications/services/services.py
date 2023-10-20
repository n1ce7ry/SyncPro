from django.db.models import Q

from applications.models import Application


def search_applications(query):
    """
    Takes a query parameter and searches for applications by name, customer names, and prices.
    Return: QuerySet
    """

    object_list = Application.objects.filter(
        Q(title__icontains=query) | Q(client__name__icontains=query) | Q(price__icontains=query)
    ).order_by('-created_at')

    return object_list