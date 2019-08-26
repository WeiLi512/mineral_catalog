from django.shortcuts import render
from .models import Mineral
from .utils import get_mineral_groups


# Create your views here.
def mineral_list(request):
    minerals = Mineral.objects.all()

    letter = request.GET.get('letter', '')
    if letter:
        minerals = Mineral.objects.filter(name__startswith=letter)

    q = request.GET.get('q', '')
    if q:
        minerals = minerals.filter(name__icontains=q)

    group = request.GET.get('group', '')
    if group:
        if group == 'Other':
            minerals = minerals.exclude(group__in=get_mineral_groups())
        else:
            minerals = minerals.filter(group=group)
    return render(request, 'list.html',
                  {'minerals': minerals, 'selected_letter': letter, 'q': q, 'selected_group': group})


def mineral_detail(request, id):
    mineral = Mineral.objects.get(id=id)
    return render(request, 'detail.html', {'mineral': mineral})
