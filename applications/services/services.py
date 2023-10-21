from datetime import date, timedelta
from calendar import monthrange

from django.db.models import Q
from django.utils import timezone

from applications.models import Application


def search_applications(query):
    """
    Takes a query parameter and searches for applications by name, customer names, and prices.
    Return: QuerySet
    """

    object_list = Application.objects.filter(
        Q(title__icontains=query) | Q(client__name__icontains=query) | Q(price__icontains=query)
    )

    return object_list.order_by('-created_at')


def filter_applications(time):
    """
    Filters applications by week, month
    Return: QuerySet
    """

    if time == 'week':
        last_week = timezone.now() - timedelta(weeks=1)
        object_list = Application.objects.filter(created_at__gte=last_week)

    elif time == 'month':
        today = date.today()
        days_in_month = monthrange(today.year, today.month)[1]
        last_month = timezone.now() - timedelta(days=days_in_month)
        object_list = Application.objects.filter(created_at__gte=last_month)

    return object_list.order_by('-created_at')