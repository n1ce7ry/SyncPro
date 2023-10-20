from tasks.models import Task, TaskStatusEnum


def tasks_filtering_by_status(status):
    """Filters tasks by status and returns QuerySet"""
    
    if status == 'created':
        object_list = Task.objects.filter(
            status=TaskStatusEnum.CREATED
        ).order_by('-created_at')
    elif status == 'in_process':
        object_list = Task.objects.filter(
            status=TaskStatusEnum.IN_PROCESS
        ).order_by('-created_at')
    else:
        object_list = Task.objects.filter(
            status=TaskStatusEnum.COMPLETED
        ).order_by('-created_at')

    return object_list
