from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return "Task: {content}".format(content=self.content)
