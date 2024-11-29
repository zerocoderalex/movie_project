from django.shortcuts import render
from .models import News_post
# Create your views here.
def index(request):
    news = News_post.objects.all()
    return render(request, 'films/index.html', {'news': news})



def new(request):
    return render(request, 'films/new.html')