from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request, 'register.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def calculator(request):
    return render(request,'calculator.html')