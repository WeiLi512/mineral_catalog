from django.shortcuts import redirect

# Create your views here.
def index(request):
    return redirect('/minerals?letter=A')
