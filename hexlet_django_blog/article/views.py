from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from django.views import View
from hexlet_django_blog.article.models import Article
from .forms import ArticleForm
# Create your views here.


class IndexView(View):
    
    template_name = 'articles/index.html'

    def get(self, request, *ar, **kw):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={'articles': articles})


class ArticleView(View):
    # с помощью функции get_object_or_404 получаем объект и пердаем его в шаблон
    def get(self, request, *ar, **kw):
        article = get_object_or_404(Article, id=kw['id'])
        return render(request, 'articles/show.html', {'article': article})


class ArticleFormCreateView(View):
    #  создаем обработчик формы с двумя методами
    def get(self, request, *ar, **kw):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})
    # метод обрабатывает данные из post-запроса и сохраняет их в базу если всё норм
    # или делает редирект на ту же страницу с передачей объекта со словарем ошибок, если не норм
    def post(self, request, *ar, **kw):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request, 'articles/create.html', {'form': form})
            
            
        
