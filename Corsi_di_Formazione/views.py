from django.shortcuts import render # type: ignore
from django.http import HttpResponse  # type: ignore
from.models import corso


def view_a(request):
    return render(request,"view_a.html")

def view_b(request):
    return render(request,"view_b.html")

def view_c(request):
    return render(request,"view_c.html")

def view_d(request):
    return render(request,"view_d.html")

def view_e(request):
    return render(request,"view_e.html")

def view_f(request):
    return render(request,"view_f.html")

def index4(request): 
    return render(request,"index4.html")




   
