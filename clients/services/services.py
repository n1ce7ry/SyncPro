from django.db.models import Q

from clients.models import Client


def search_clients(query):
    """
    Takes a query parameter and searches by it among the name, phone, and mail of customers.
    Return: QuerySet
    """
    object_list = Client.objects.filter(
        Q(name__icontains=query) | Q(phone__icontains=query) | Q(email__icontains=query)
    )
    return object_list