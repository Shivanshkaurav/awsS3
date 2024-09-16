from django.shortcuts import render
from .models import *

def index(request):
    data = Student.objects.all()
    context = {'data': data}
    return render(request, 'index.html', context)