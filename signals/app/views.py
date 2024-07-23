from django.shortcuts import render
from .models import *
from .form import Mymodelform   

# Create your views here.

def index(request):
    return render(request,"index.html")

def ragistration(request):
    form = Mymodelform(request.POST or None)
    if form.is_valid()
