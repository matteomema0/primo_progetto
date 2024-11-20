from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,"welcome.html")

def homepage(request):
    return render(request,"homepage.html")

def lista(request):
    return render(request,"lista.html")

def chi_siamo(request):
    return render(request,"chi_siamo.html")