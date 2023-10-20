from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    phone = models.IntegerField()
    email = models.EmailField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return '/clients/'