from django.db import models


class TaskStatusEnum(models.TextChoices):
    CREATED = 'Создано'
    IN_PROCESS = 'В процессе'
    COMPLETED = 'Завершено'

    
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    status = models.CharField(
        choices=TaskStatusEnum.choices,
        default=TaskStatusEnum.CREATED,
        max_length=32,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    
    def get_absolute_url(self):
        return '/tasks/'
    
    def __str__(self):
        return self.title
