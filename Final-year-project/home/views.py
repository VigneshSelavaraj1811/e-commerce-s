# Create your views here.
from django.shortcuts import render


def home(request):
    context = {}
    template = 'home/home.html'
    return render(request, template, context)
