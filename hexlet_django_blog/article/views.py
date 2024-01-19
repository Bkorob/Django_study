from django.shortcuts import render
from django.http import HttpResponse
# from django.views import View
# Create your views here.


def article(request, tags, article_id):
    return HttpResponse(f'Статья № {article_id}. Тег {tags}')
# class ArticleView(View):
#     def get(self, request, *a, **kw):
#         return render(request, 'articles/index.html', context={'name': 'article'})
