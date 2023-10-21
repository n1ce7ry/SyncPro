from applications.models import Application
from clients.models import Client

from django.db.models import Sum, OuterRef


def get_customer_statistics():
    """
    The service that determines how much money a client has brought in.
    Return: QuerySet
    """
    query = Client.objects.all().values('id', 'name', 'phone').annotate(
        client_impact=Sum(
            Application.objects.filter(
                client=OuterRef('id')
            ).values('price')
        )
    ).order_by('-client_impact')

    return query