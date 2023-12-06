from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    create_at = models.DateField(auto_now_add=True, null=False, blank=False)
    dead_line = models.DateTimeField(null=False, blank=False)
    finshed_at = models.DateTimeField(null=True)
