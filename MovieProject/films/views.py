from django.shortcuts import render
from .models import News_post
# Create your views here.
def home(request):
    news = News_post.objects.all()
    return render(request, 'films/index.html', {'films': news})

def create_news(request):
    return render(request, 'films/add_new_post.html')

