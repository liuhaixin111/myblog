from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import blog.models

def index(request):
    articles = blog.models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def artile_page(request, article_id):
    article = blog.models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})