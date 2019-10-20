from django.shortcuts import render, get_object_or_404
from .models import Conocimiento

# Create your views here.

def homepage(request):
    conocimientos = Conocimiento.objects
    return render(request, 'conocimientos/home.html', {'conocimientos': conocimientos})

def detail(request, conocimiento_id):
    conocimiento_detail = get_object_or_404(Conocimiento, pk=conocimiento_id)
    return render(request, 'conocimientos/detail.html', {'conocimiento':conocimiento_detail})