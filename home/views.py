from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dests = Destination.objects.all()
    # print(dests)
    return render(request, 'index.html', {'destinations': dests})