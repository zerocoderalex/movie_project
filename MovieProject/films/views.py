from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'films/index.html')

def new(request):
    return render(request, 'films/new.html')