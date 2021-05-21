from django.db import models

# Create your models here.
class Item(models.models):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    send_notifications = models.BooleanField(default=False)
    hide = models.BooleanField(default=False)

    class Meta:
        abstract = True

class TodoList(Item):
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name='sub_lists')

class TodoItem(Item):
    due_date = models.DateTimeField()
    send_notifications = models.BooleanField(default=False)
    # https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='items')


