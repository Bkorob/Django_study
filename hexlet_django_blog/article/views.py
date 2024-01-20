from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
# Create your views here.


def article(request, tags, article_id):
    return render(request, 'articles/psevdohome.html', {'tag': tags, 'art': article_id})
class ArticleView(View):
    def get(self, request):
        return redirect('article', tags='python', article_id=42)
