from django.shortcuts import render
from .models import Mineral

# Create your views here.
def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'list.html', {'minerals': minerals})

def mineral_detail(request, id):
    mineral = Mineral.objects.get(id=id)
    return render(request, 'detail.html', {'mineral': mineral})