import json
from datetime import date, timedelta
from calendar import monthrange

from django.utils import timezone
from django.db.models import Sum, Count

from applications.models import Application
from dashboard.services.services import get_day_abbr


def get_finance_statistics():
    qs = Application.objects.all().values('price', 'created_at').order_by('-created_at')
    return qs


def get_statistics_by_month(context):
    """
    The service generates context for application statistics.
    """
    week = _get_current_week()
    month = _get_current_month()

    total_applications = Application.objects.filter(created_at__gte=month).aggregate(
        app_by_month=Count("id")
    )
    total_applications_revenue = Application.objects.filter(created_at__gte=month).aggregate(
        revenue_by_month=Sum("price")
    )

    context['data'] = json.dumps(
        [
            {
                'day': get_day_abbr(obj['day']),
                'count': obj['count'],
            }
            for obj in Application.objects.filter(created_at__gte=week).extra(
                {'day': "date(created_at)"}
            ).values('day').annotate(count=Sum('price'))
        ]
    )

    context["now"] = timezone.now()
    context["total_app"] = total_applications
    context["total_price"] = total_applications_revenue
    return context


def _get_current_week():
    current_week = timezone.now() - timedelta(weeks=1)
    return current_week


def _get_current_month():
    today = date.today()
    days_in_month = monthrange(today.year, today.month)[1]
    current_month = timezone.now() - timedelta(days=days_in_month)
    return current_month