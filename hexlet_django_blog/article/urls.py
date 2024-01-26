from django.urls import path
from .views import IndexView, article, ArticleView


urlpatterns = [
    # path('<str:tags>/<int:article_id>', article, name='article'),
    path('', IndexView.as_view(), name='articles'),
    path('<int:id>/', ArticleView.as_view(), name='article'),
]