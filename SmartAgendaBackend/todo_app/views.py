from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse(f"Hello Folks");

def list_todos(request, provided_name):
    return HttpResponse(f"Bonjour {provided_name}, récupération des listes de tâches à faire en cours ...")

