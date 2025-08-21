from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("doing", "Doing"),
        ("done", "Done"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="todo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
