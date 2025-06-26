from django.shortcuts import render
from .models import News_post

def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news_home.html', {'news':news})
