from datetime import date, timedelta
from calendar import monthrange

from django.db.models import Q

from applications.models import Application


START_DAY = date.today()


def search_applications(query):
    """
    Takes a query parameter and searches for applications by name, customer names, and prices.
    Return: QuerySet
    """

    object_list = Application.objects.filter(
        Q(title__icontains=query) | Q(client__name__icontains=query) | Q(price__icontains=query)
    )

    return object_list.order_by('-created_at')


def filter_applications(date):
    """
    Filters applications by week, month
    Return: QuerySet
    """

    if date == 'week':
        enddate = START_DAY + timedelta(days=7)
        object_list = Application.objects.filter(created_at__range=[START_DAY, enddate])

    elif date == 'month':
        days_in_month = monthrange(START_DAY.year, START_DAY.month)[1]
        enddate = START_DAY + timedelta(days=days_in_month)
        object_list = Application.objects.filter(created_at__range=[START_DAY, enddate])

    return object_list.order_by('-created_at')