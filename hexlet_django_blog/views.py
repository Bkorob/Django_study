from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={
        'who': 'djano',
        'eve': "Hello, World!",
        })


def about(request):
    return render(request, 'about.html')


