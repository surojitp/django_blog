from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Surojit',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 5, 2018'
    },
    {
        'author': 'Bikash',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 10, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
