from django.shortcuts import render
from django.views.generic import ListView
from .models import Pila

# Create your views here.

class HomePageView(ListView):
    model = Pila
    template_name = 'home.html'
    context_object_name = 'listado'

