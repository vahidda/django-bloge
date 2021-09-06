from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import models

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("Hello, world. You're at the vahid index.")


def home(request):
    return render(request, 'home.html')
    # return HttpResponse('home')


def articleslist(request):
    articles=models.Articles.objects.all().order_by('date')
    args={'articles':articles}
    return render(request, 'articles/articleslist.html',args)
