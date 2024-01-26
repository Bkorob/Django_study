from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from hexlet_django_blog.article.models import Article
# Create your views here.


class IndexView(View):
    
    template_name = 'articles/index.html'

    def get(self, request, *ar, **kw):
        articles = Article.objects.all()[:5]
        return render(request, 'articles/index.html', context={'articles': articles})


def article(request, tags, article_id):
    return render(request, 'articles/psevdohome.html', {'tag': tags, 'art': article_id})


class ArticleView(View):
    def get(self, request, *ar, **kw):
        article = get_object_or_404(Article, id=kw['id'])
        return render(request, 'articles/show.html', {'article': article})
