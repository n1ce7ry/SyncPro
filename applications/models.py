from django.db import models

from clients.models import Client


class Application(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    title = models.CharField(max_length=255)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return '/applications/'