from logging import error

from django.shortcuts import render, redirect
from .models import News_post
from .forms import News_postForm

# Create your views here.
def home(request):
    films = News_post.objects.all()
    return render(request, 'films/index.html', {'films': films})

def create_news(request):
         error=''
         if request.method == 'POST':
                 form = News_postForm(request.POST) # Сюда сохранится информация от пользователя.
                 if form.is_valid():
                         form.save()
                         return redirect('home')
                 else:
                         error # "Данные были заполнены некорректно"
         form = News_postForm()
         return render(request, 'films/add_new_post.html', {'form': form, 'error': error})










