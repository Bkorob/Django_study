from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView


def index(request): 
    
    'article_id': article_id,
    'tags': tags
    return redirect(request, 'index.html', context={
        )
# class HomePageView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context['who'] = 'djano'
#         context['eve'] = "Hello, World!"
#         return context


# def about(request):
#     return render(request, 'about.html')


