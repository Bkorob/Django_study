from django.urls import path
from .views import IndexView, article


urlpatterns = [
    path('<str:tags>/<int:article_id>', article, name='article'),
    path('', IndexView.as_view()),
]