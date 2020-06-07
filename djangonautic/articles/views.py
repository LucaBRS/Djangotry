####IMPORTANTE registrare l'app allinterno di settings del main project

from django.shortcuts import render
from .models import Article
# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles':articles}) # pre farlo vedere registrarlo nell url principale 