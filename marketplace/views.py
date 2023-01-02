from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')
    
def login(request):
    return render(request,'login.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def tc(request):
    return render(request,'t&c.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')

def marketplace(request):
    return render(request,'marketplace.html')

def property(request):
    return render(request,'singleproperty.html')