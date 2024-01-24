from django.shortcuts import render, redirect
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


# class ArticleView(View):
#     def get(self, request):
#         return redirect('article', tags='python', article_id=42)
