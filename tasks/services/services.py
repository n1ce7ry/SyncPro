from tasks.models import Task, TaskStatusEnum


def tasks_filtering_by_status(status):
    """
    Filters tasks by status
    Return: QuerySet
    """
    
    if status == 'created':
        object_list = Task.objects.filter(status=TaskStatusEnum.CREATED)

    elif status == 'in_process':
        object_list = Task.objects.filter(status=TaskStatusEnum.IN_PROCESS)

    else:
        object_list = Task.objects.filter(status=TaskStatusEnum.COMPLETED)

    return object_list.order_by('-created_at')