from django.shortcuts import render
from .models import Producto
from django.http import HttpResponse

def index(req):
    
    return HttpResponse('todo ok')

