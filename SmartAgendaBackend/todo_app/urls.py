from django.urls import path
from todo_app import views
# from django.conf.urls import url

urlpatterns = [
    # learn regular expression: https://openclassrooms.com/en/courses/4425111-perfectionnez-vous-en-python/4464009-utilisez-des-expressions-regulieres
    # url(r'^(?P<provided_name>[a-z|A-Z]+)/$', views.list_todos, name="list_todos")
    path('<str:provided_name>/',views.list_todos, name="list_todos")
]