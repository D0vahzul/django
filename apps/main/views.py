from django.shortcuts import render
from .models import Header

def index(request):
    header = Header.objects.all()
    return render(request, 'pages/index.html', {'header': header})
