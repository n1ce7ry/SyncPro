import json
import calendar
from datetime import timedelta

from applications.models import Application
from tasks.models import Task, TaskStatusEnum
from clients.models import Client

from django.utils import timezone
from django.db.models import Sum, OuterRef, Subquery, Count, Q


def get_customer_statistics():
    """
    The service that determines how much money a client has brought in.
    Return: QuerySet
    """
    query = Client.objects.all().annotate(
        client_impact=Subquery(
            Application.objects.filter(client=OuterRef('id'))
            .values('client')
            .annotate(total_price=Sum('price'))
            .values('total_price')[:1]
    )
    ).order_by('-client_impact')

    return query[:10]


def get_summarize_all_section(context):
    """
    The service forming a contex with a summary of information from all sections
    """
    week = _get_current_week()

    task_data = Task.objects.aggregate(
        total_tasks=Count('id'),
        total_tasks_completed=Count('id', filter=Q(status=TaskStatusEnum.COMPLETED))
    )

    latest_tasks = Task.objects.all().order_by('-created_at')[:4]

    context['finance_data'] = json.dumps(
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

    context['application_data'] = json.dumps(
        [
            {
                'day': get_day_abbr(obj['day']),
                'count': obj['count'],
            }
            for obj in Application.objects.filter(created_at__gte=week).extra(
                {'day': "date(created_at)"}
            ).values('day').annotate(count=Count('id'))
        ]
    )

    context["now"] = timezone.now()
    context["task_data"] = task_data
    context["latest_tasks"] = latest_tasks
    return context


def get_day_abbr(date: str) -> str:
    weekday_names = ['Пн', 'Вт', 'Cр', 'Чт', 'Пт', 'Сб', 'Вс']

    year, month, day = tuple(map(int, date.split('-')))
    weekday = calendar.weekday(year, month, day)
    weekday_name = weekday_names[weekday]

    return weekday_name


def _get_current_week():
    current_week = timezone.now() - timedelta(weeks=1)
    return current_week