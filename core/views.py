from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def contact(request):
    return render(request,'core/contacts.html')

def about(request):
    return render(request,'core/about.html')


